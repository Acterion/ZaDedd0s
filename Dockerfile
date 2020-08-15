FROM python:3.8-slim

WORKDIR /code

COPY Pipfile* /tmp/

RUN pip install pipenv
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN pip uninstall --yes pipenv

COPY src/ .

CMD ["python", "./main.py"]