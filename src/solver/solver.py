import asyncio
import aiohttp

sample_captcha = """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"""

class Solver:
    def __init__(self):
        self._solution = ''
        self._task_id = 0

    async def solve_captcha(self, captcha_string):
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


solver = Solver()
res = asyncio.run(solver.solve_captcha(sample_captcha))
print(res)
