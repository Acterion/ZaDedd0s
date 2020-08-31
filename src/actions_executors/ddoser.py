import asyncio

import aiohttp
from aiohttp_socks import ProxyConnector

import atexit
from src.actions_executors.iexecutors import IDdoser, PersonInfo
from src.statistics.istatistics import IDdoserStatistics


class Ddoser(IDdoser):
    def __init__(self, city_data: dict = None, cookies: dict = None, stat: IDdoserStatistics = None):
        self._headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Accept-Language': 'ru-RU'
        }
        self._data = {
            'locationCode': 'jeka',
            'realmId': '881',
            'categoryId': '1677',
            'date': '22.08.2020',
            'dateStr': '22.08.2020'
        }
        if city_data:
            self._data = {**self._data, **city_data}

        self._domain = 'https://service2.diplo.de/rktermin/'
        self._month_url = 'https://service2.diplo.de/rktermin/extern/appointment_showMonth.do'
        self._final_url = 'https://service2.diplo.de/rktermin/extern/appointment_showForm.do'
        self._cookies = cookies
        self._socks = 'socks5://127.0.0.1:9050'
        self._proxy_conn = ProxyConnector.from_url(self._socks)
        self._session = aiohttp.ClientSession(cookies=self._cookies, connector=self._proxy_conn)
        self._refresh_cookies()
        self._stat = stat
        atexit.register(self.cleanup)

    def cleanup(self):
        self._session.close()

    def _refresh_cookies(self):
        self._session.cookie_jar.clear()
        asyncio.get_event_loop().call_later(3600, self._refresh_cookies)

    async def get_month(self, date: str, solved_captcha: str = None) -> str:
        self._data['captchaText'] = solved_captcha
        self._data['date'] = date
        self._data['dateStr'] = date
        try:
            async with self._session.post(self._month_url, data=self._data, headers=self._headers) as r:
                self._data.pop('captchaText', None)
                self._stat.add_page_update()
                return await r.text()
        except aiohttp.ClientConnectionError as e:
            print('Client connection error -> ', e)

    async def get_day(self, day_href: str) -> str:
        day_href = self._domain + day_href
        async with self._session.get(day_href, headers=self._headers) as r:
            return await r.text()

    async def get_time_slot(self, time_href: str) -> str:
        time_href = self._domain + time_href
        async with self._session.get(time_href, headers=self._headers) as r:
            return await r.text()

    async def send_final_form(self, solved_captcha: str, hidden_fields: dict, person_info: PersonInfo) -> str:
        self._data['captchaText'] = solved_captcha
        self._data = {**self._data, **person_info._asdict()}
        self._data['emailrepeat'] = person_info.email
        self._data['fields[0].content'] = person_info.residence
        self._data['fields[1].content'] = person_info.passport
        self._data['fields[2].content'] = 'Studium'
        self._data = {**self._data, **hidden_fields}
        async with self._session.post(self._final_url, data=self._data, headers=self._headers) as r:
            return await r.text()
