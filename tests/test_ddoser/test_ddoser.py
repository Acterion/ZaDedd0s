import pytest

from src.actions_executors.ddoser import Ddoser
import tests.test_ddoser.samples as samples


@pytest.mark.asyncio
async def closed_test_get_month_without_captcha():
    cookies = {
        'JSESSIONID': '5833E1F56C52F87563FDEEC5A3477F19',
        'KEKS': 'TERMIN325'
    }
    d = Ddoser(samples.data_nowo, cookies)
    await d.get_month('20.08.2020', '865y26')
    await d.get_day('extern/appointment_showDay.do?locationCode=nowo&realmId=1098&categoryId=2266&dateStr=26.08.2020')
    print(await d.get_time_slot('extern/appointment_showForm.do?locationCode=nowo&realmId=1098&categoryId=2266&dateStr=26.08.2020&openingPeriodId=51092'))
