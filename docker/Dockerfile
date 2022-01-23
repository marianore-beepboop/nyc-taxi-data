FROM python:3.9

RUN pip install poetry
ENV PATH="/root/.local/pipx/venvs/poetry/bin/:$PATH"

COPY pyproject.toml /project/pyproject.toml

WORKDIR /project
RUN poetry install --no-root
COPY . /project
RUN poetry install --no-interaction
