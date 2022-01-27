FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src

RUN apt update && python -m pip install --upgrade pip
RUN python -m pip install poetry

COPY ./web_app web_app
COPY ./launch_app.sh /usr/src
COPY ./pyproject.toml /usr/src

RUN poetry config virtualenvs.create false && poetry lock && poetry install

EXPOSE 8000

ENTRYPOINT ["bash", "launch_app.sh"]