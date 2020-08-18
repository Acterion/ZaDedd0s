import aiohttp
from src.ddoser.iddoser import IDdoser, PersonInfo


class Ddoser(IDdoser):
    def __init__(self):
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
        self._domain = 'https://service2.diplo.de/rktermin/'
        self._month_url = 'https://service2.diplo.de/rktermin/extern/appointment_showMonth.do'
        self._final_url = 'https://service2.diplo.de/rktermin/extern/appointment_showForm.do'

    async def get_month(self, date: str, solved_captcha: str = None) -> str:
        self._data['captchaText'] = solved_captcha
        self._data['date'] = date
        self._data['dateStr'] = date
        async with aiohttp.ClientSession() as session:
            async with session.post(self._month_url, data=self._data, headers=self._headers) as r:
                self._data.pop('captchaText')
                return await r.text()

    async def get_day(self, day_href: str) -> str:
        day_href = self._domain + day_href
        async with aiohttp.ClientSession() as session:
            async with session.post(day_href, data=self._data, headers=self._headers) as r:
                return await r.text()

    async def get_time_slot(self, time_href: str) -> str:
        time_href = self._domain + time_href
        async with aiohttp.ClientSession() as session:
            async with session.post(time_href, data=self._data, headers=self._headers) as r:
                return await r.text()

    async def send_final_form(self, solved_captcha: str, hidden_fields: dict, person_info: PersonInfo) -> str:
        self._data['captchaText'] = solved_captcha
        self._data = {**self._data, **person_info._asdict()}
        self._data['emailrepeat'] = person_info.email
        self._data['fields[0].content'] = person_info.residence
        self._data['fields[1].content'] = person_info.passport
        self._data['fields[2].content'] = 'Studium'
        self._data = {**self._data, **hidden_fields}
        async with aiohttp.ClientSession() as session:
            async with session.post(self._final_url, data=self._data, headers=self._headers) as r:
                return await r.text()
