#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

# update package managers
sudo apt-get -y update

# install nginx
sudo apt-get -y install nginx

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

# creating symbolic link
target="/data/web_static/releases/test/"
link="/data/web_static/current"

# Check if the symbolic link already exists and delete it
if [ -L "$link" ]; then
    sudo rm -r "$link"
fi

# Create the symbolic link
sudo ln -sfn "$target" "$link"

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