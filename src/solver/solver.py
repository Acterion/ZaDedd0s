import aiohttp


class Solver:
    def __init__(self):
        self._solution = ''
        self._task_id = 0
        self._headers = {
            'Content-Type': 'application/json',
            'Connection': 'keep-alive'
        }
        self._create_task_url = 'https://api.anti-captcha.com/createTask'
        self._create_task_data = {
                'clientKey': '5612b49bb41267b5a66d442e6fe2ee0a',
                'task': {
                    'type': 'ImageToTextTask',
                    'body': '',
                    'phrase': False,
                    'case': False,
                    'numeric': 0,
                    'math': False,
                    'minLength': 0,
                    'maxLength': 0
                }
        }
        self._get_result_url = 'https://api.anti-captcha.com/getTaskResult'
        self._task_id_data = {
                'clientKey': '5612b49bb41267b5a66d442e6fe2ee0a',
                'taskId': self._task_id
            }
        self._report_url = 'https://api.anti-captcha.com/reportIncorrectImageCaptcha'

    async def solve_captcha(self, captcha_string):

        async with aiohttp.ClientSession() as session:
            self._create_task_data['body'] = captcha_string
            async with session.post(self._create_task_url, json=self._create_task_data, headers=self._headers) as resp:
                self._task_id = (await resp.json())['taskId']

            status = ''
            while status != 'ready':
                async with session.post(self._get_result_url, json=self._task_id_data, headers=self._headers) as resp:
                    status = (await resp.json())['status']
                    self._solution = (await resp.json())

        return self._solution['solution']['text']

    async def report_incorrect(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(self._report_url, json=self._task_id_data, headers=self._headers) as resp:
                return (await resp.json())['status'] is "success"
