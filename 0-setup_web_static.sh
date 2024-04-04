#!/usr/bin/env bash
# Install nginx and create directories
sudo apt-get update
sudo apt-get install -y nginx

directories=("/data/" "/data/web_static/" "/data/web_static/releases/" "/data/web_static/shared/" "/data/web_static/releases/test/")

for dir in "${directories[@]}"; do
    if [ ! -d "$dir" ]; then
        sudo mkdir -p "$dir"
    fi
done

cat <<EOF /data/web_static/releases/test/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
run("sudo chwon -R ubuntu:ubuntu /data/")

cat <<EOF /etc/nginx/sites-available/default
server {
    location /hbnb_static {
        alias /data/web_static/current/;
    }
}
EOF