FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV TZ=America/Sao_Paulo

WORKDIR /var/www/public/

COPY . /var/www/public/

RUN mkdir -p /var/www/public/staticfiles/
RUN chmod 644 /var/www/public/staticfiles/
RUN mkdir -p /var/www/public/medias/
RUN chmod 777 /var/www/public/medias/

RUN apk add --no-cache build-base postgresql-dev gcc musl-dev tzdata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x /var/www/public/start.sh
ENTRYPOINT [ "sh", "-c", "./start.sh" ]

EXPOSE 8000