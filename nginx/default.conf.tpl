upstream servers {

    server django:8000;

}

server {

    listen 80;
    server_name 0.0.0.0 sgg.isanocci.com.br;

    include /etc/nginx/mime.types;

    location / {
        proxy_pass http://servers;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
    }

    location /assets/static/ {
        alias /var/www/public/staticfiles/;
        autoindex on;
        expires 30d;
    }

    location /assets/media/ {
        alias /var/www/public/media/;
        autoindex on;
        expires 30d;
    }

    location /adminer/ {
        proxy_pass http://adminer:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

}