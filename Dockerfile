FROM python:3.8-slim

WORKDIR /code

ENV bot_token="1341472761:AAHLr7PHKzJ7iuN0-jsO_APimJ6KY76YoOk"

RUN pip install pipenv

COPY Pipfile* /tmp/

RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY src/ .

CMD ["python", "./main.py"]