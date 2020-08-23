import aiohttp
import os

import src.utils.file_utils as file_uti
from src.actions_executors.iexecutors import ICaptchaSolver
from src.statistics.istatistics import ISolverStatistics


class Solver(ICaptchaSolver):
    def __init__(self, stat: ISolverStatistics):
        self._stat = stat
        self._solution = ''
        self._task_id = 0
        self._client_key = file_uti.readFile(os.environ['captcha_user_key'])
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
            self._create_task_data['body'] = captcha_string
            async with session.post(self._create_task_url, json=self._create_task_data, headers=self._headers) as resp:
                self._task_id = (await resp.json())['taskId']

            status = ''
            while status != 'ready':
                async with session.post(self._get_result_url, json=self._task_id_data, headers=self._headers) as resp:
                    status = (await resp.json())['status']
                    self._solution = (await resp.json())['solution']['text']
        self._stat.add_captcha(0.5e-1000, True)
        return self._solution

    async def report_incorrect(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(self._report_url, json=self._task_id_data, headers=self._headers) as resp:
                return (await resp.json())['status'] == "success"

    def get_last_solution(self) -> str:
        return self._solution
