FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /var/www/public/

COPY . /var/www/public/

RUN apk add --no-cache build-base postgresql-dev gcc musl-dev

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "sh", "-c", "./start.sh" ]