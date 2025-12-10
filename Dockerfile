FROM python:3.14

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH .
ENV UV_NO_DEV=1

RUN apt-get update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:0.9.17 /uv /uvx /bin/

COPY uv.lock pyproject.toml ./
COPY README.md Makefile ./

RUN uv sync --locked

COPY src src
COPY scripts scripts

RUN chmod a+x scripts/*

CMD [ "./scripts/entrypoint.sh" ]
