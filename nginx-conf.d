upstream app {
    server app:8500;
}

server {
    listen 50;

    location / {
        proxy_pass http://app;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;
    }

    location /staticfiles/ {
        alias /var/www/html/staticfiles/;
    }
}