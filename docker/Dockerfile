FROM python:3.11-slim-bookworm

RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin curl


COPY pyproject.toml ./pyproject.toml
COPY poetry.lock ./poetry.lock
# Install poetry and dependencies
ENV POETRY_HOME "/opt/poetry"
ENV PATH "$POETRY_HOME/bin:$PATH"

ENV PATH /root/.local/bin:$PATH

RUN curl -sSL https://install.python-poetry.org/ | python3 -

RUN POETRY_VIRTUALENVS_CREATE=false poetry install
WORKDIR /usr/src/
COPY todo_site ./todo_site
WORKDIR /usr/src/todo_site/
