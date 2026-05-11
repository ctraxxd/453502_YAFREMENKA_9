FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    git ca-certificates \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN git clone --depth 1 https://github.com/smartiqaorg/geometric_lib.git /opt/geometric_lib

ENV PYTHONPATH="/opt/geometric_lib:${PYTHONPATH}"

COPY app.py .

CMD ["python", "app.py", "sh"]