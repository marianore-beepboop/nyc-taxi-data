FROM python:3.9

RUN pip install pipx
RUN pipx install poetry
ENV PATH="/root/.local/pipx/venvs/poetry/bin/:$PATH"

COPY pyproject.toml poetry.lock /project/
COPY .google/credentials/google_credentials.json /project/.google/credentials/

WORKDIR /project
RUN poetry install --no-root
COPY . /project
RUN poetry install --no-interaction
