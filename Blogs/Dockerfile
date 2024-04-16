FROM python:3.12

COPY poetry.lock pyproject.toml ./

RUN pip install poetry

RUN poetry install

COPY . .

EXPOSE 80

