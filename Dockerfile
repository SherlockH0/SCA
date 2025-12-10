FROM python:3.14

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH .

RUN apt-get update \
    && curl -LsSf https://astral.sh/uv/0.9.17/install.sh | sh \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY uv.lock pyproject.toml ./
COPY README.md Makefile ./

RUN uv sync

COPY src src
COPY scripts scripts

RUN chmod a+x scripts/*

CMD [ "./scripts/entrypoint.sh" ]
