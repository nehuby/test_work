FROM python

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT [ "bash", "/usr/src/app/entrypoint.sh" ]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]