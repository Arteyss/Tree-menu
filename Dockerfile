FROM python:3.10.11-alpine

RUN pip install poetry

WORKDIR /tree-menu

COPY . .

RUN poetry config virtualenvs.create false \
  && poetry install --no-dev

WORKDIR /tree-menu/DjangoApp

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
