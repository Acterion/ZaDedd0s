import aiohttp


class Solver:
    def __init__(self):
        self._solution = ''
        self._task_id = 0

    async def solve_captcha(self, captcha_string):
        """Creates task and awaits for its result, returns solution"""

        headers = {
            'Content-Type': 'application/json',
            'Connection': 'keep-alive'
        }
        async with aiohttp.ClientSession() as session:
            """Create task"""
            url = 'https://api.anti-captcha.com/createTask'
            data = {
                'clientKey': '5612b49bb41267b5a66d442e6fe2ee0a',
                'task': {
                    'type': 'ImageToTextTask',
                    'body': captcha_string,
                    'phrase': False,
                    'case': False,
                    'numeric': 0,
                    'math': False,
                    'minLength': 0,
                    'maxLength': 0
                }
            }
            async with session.post(
                url,
                json=data,
                headers=headers
            ) as resp:
                self._task_id = (await resp.json())['taskId']

            """Wait for task result and write it to _solution"""
            url = 'https://api.anti-captcha.com/getTaskResult'
            data = {
                'clientKey': '5612b49bb41267b5a66d442e6fe2ee0a',
                'taskId': self._task_id
            }
            status = ''
            while status != 'ready':
                async with session.post(
                    url,
                    json=data,
                    headers=headers
                ) as resp:
                    status = (await resp.json())['status']
                    self._solution = (await resp.json())

        return self._solution['solution']['text']

    async def report_incorrect(self):
        """Reports last task as incorrect"""

        headers = {
            'Content-Type': 'application/json',
            'Connection': 'keep-alive'
        }
        async with aiohttp.ClientSession() as session:
            url = 'https://api.anti-captcha.com/reportIncorrectImageCaptcha'
            data = {
                'clientKey': '5612b49bb41267b5a66d442e6fe2ee0a',
                'taskId': self._task_id
            }
            async with session.post(
                url,
                json=data,
                headers=headers
            ) as resp:
                return (await resp.json())['status'] is "success"
