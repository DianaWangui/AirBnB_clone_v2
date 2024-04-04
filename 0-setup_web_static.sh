#!/usr/bin/env bash
# update packages abd install nginx and create directories
sudo apt-get -y update
sudo apt-get install -y nginx

# directories and files 
#creating directories
directories=("/data/" "/data/web_static/" "/data/web_static/releases/" "/data/web_static/shared/" "/data/web_static/releases/test/")
for dir in "${directories[@]}"; do
    if [ ! -d "$dir" ]; then
        sudo mkdir -p "$dir"
    fi
done

# create html file
sudo tee /data/web_static/releases/test/index.html > /dev/null << EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# Check if the symbolic link already exists and delete it
rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current

# giving owndership of data directory to user and group ubuntu
sudo chown -R ubuntu:ubuntu /data/

sudo tee /etc/nginx/sites-available/default >/dev/null <<EOF
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