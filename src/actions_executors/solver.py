import aiohttp

from src.actions_executors.iexecutors import ICaptchaSolver
from src.statistics.istatistics import ISolverStatistics


class Solver(ICaptchaSolver):
    def __init__(self, stat: ISolverStatistics, user_key):
        self._stat = stat
        self._solution = ''
        self._task_id = 0
        self._client_key = user_key
        self._headers = {
            'Content-Type': 'application/json',
            'Connection': 'keep-alive'
        }
        self._create_task_url = 'https://api.anti-captcha.com/createTask'
        self._create_task_data = {
                'clientKey': self._client_key,
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
                'clientKey': self._client_key,
                'taskId': self._task_id
            }
        self._report_url = 'https://api.anti-captcha.com/reportIncorrectImageCaptcha'

    async def solve(self, captcha_string):
        async with aiohttp.ClientSession() as session:
            self._create_task_data['task']['body'] = captcha_string
            async with session.post(self._create_task_url, json=self._create_task_data, headers=self._headers) as resp:
                response = await resp.json()
                self._task_id = response.get('taskId')
                error = response.get('errorId')
                if not self._task_id or error:
                    return None
                self._task_id_data['taskId'] = self._task_id

            status = ''
            error = 0
            response = None
            while status != 'ready':
                async with session.post(self._get_result_url, json=self._task_id_data, headers=self._headers) as resp:
                    response = await resp.json()
                    status = response.get('status')
                    error = response.get('errorId')

            if not error:
                self._solution = response['solution']['text']
                self._stat.add_captcha(float(response['cost']), True)

        return self._solution

    async def report_incorrect(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(self._report_url, json=self._task_id_data, headers=self._headers) as resp:
                return (await resp.json())['status'] == 'success'

    def get_last_solution(self) -> str:
        return self._solution
