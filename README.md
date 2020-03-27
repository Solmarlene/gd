## Deployment

Following steps presume vanilla AWS Ubuntu 18.

### Install pre-requisites

```console
ubuntu@host:~$ sudo apt-get update
ubuntu@host:~$ sudo apt install python3-pip nginx gunicorn3
ubuntu@host:~$ pip3 install Django spacy
ubuntu@host:~$ python3 -m spacy download es_core_news_md
```


### Get source code

```console
ubuntu@host:~$ git clone https://github.com/Solmarlene/gd 
# Edit gd/gd/settings.py to specify a long and unique SECRET_KEY and correct ALLOWED_HOSTS.
```


### Provide configuration files

```ini
# In /etc/systemd/system/gunicorn.service:
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
Type=notify
User=ubuntu
Group=ubuntu
RuntimeDirectory=gunicorn3
WorkingDirectory=/home/ubuntu/gd
ExecStart=/usr/bin/gunicorn3 gd.wsgi
ExecReload=/bin/kill -s HUP $MAINPID
KillMode=mixed
TimeoutStopSec=25
TimeoutSec=900
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

```ini
# In /etc/systemd/system/gunicorn.socket:
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/tmp/gunicorn.sock
User=www-data
# Mode=600

[Install]
WantedBy=sockets.target
```

```nginx
# In /etc/nginx/nginx/conf:
worker_processes 1;

user nobody nogroup;
error_log  /var/log/nginx/error.log warn;
pid /var/run/nginx.pid;

events {
  worker_connections 1024;
  accept_mutex off;
}

http {
  include mime.types;
  default_type application/octet-stream;
  access_log /var/log/nginx/access.log combined;
  sendfile on;

  upstream app_server {
    server unix:/tmp/gunicorn.sock fail_timeout=0;
  }

  server {
    # if no Host match, close the connection to prevent host spoofing
    listen 80 default_server;
    return 444;
  }

  server {
    listen 80;
    client_max_body_size 4G;

    # set the correct host(s) for your site
    # server_name example.com;

    keepalive_timeout 5;

    location / {
      try_files $uri @proxy_to_app;
    }

    location @proxy_to_app {
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Proto $scheme;
      proxy_set_header Host $http_host;
      proxy_redirect off;
      proxy_pass http://app_server;
    }
  }
}
```


### Reload services

```console
ubuntu@host:~$ sudo systemctl daemon-reload
ubuntu@host:~$ sudo service nginx restart
ubuntu@host:~$ sudo service gunicorn start
```
