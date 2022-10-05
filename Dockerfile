FROM python:3.8 as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD . /code
WORKDIR /code


COPY Pipfile Pipfile.lock ./

RUN pip install --no-cache-dir pipenv && pipenv install --dev --system --deploy

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
