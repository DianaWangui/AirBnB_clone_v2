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

sudo tee /data/web_static/releases/test/index.html > /dev/null <<EOF
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

sudo tee /etc/nginx/sites-available/default > /dev/null <<EOF
server {
        listen 80;
        listen [::]:80 default_server;
        server_name _;
        add_header X-Served-By "${HOSTNAME}";
        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
        location @404 {
                 return 404 "Ceci n'est pas une page.";
        }

        location /hbnb_static {
                 alias /data/web_static/current/;
        }


        root /var/www/html;
        error_page 404 = @404;
}
EOF
sudo service nginx restart