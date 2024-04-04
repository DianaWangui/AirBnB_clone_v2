#!/usr/bin/env bash
# update packages abd install nginx and create directories
sudo apt-get -y update
sudo apt-get install -y nginx

# directories and files 
directories=("/data/" "/data/web_static/" "/data/web_static/releases/" "/data/web_static/shared/" "/data/web_static/releases/test/")

# loops through to check if they exist if not create them
for dir in "${directories[@]}"; do
    if [ ! -d "$dir" ]; then
        sudo mkdir -p "$dir"
    fi
done

# create a fake html file and append to the index.html file
sudo tee /data/web_static/releases/test/index.html > /dev/null <<EOF
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

# change ownership of the /data/ folder
sudo chwon -R ubuntu:ubuntu /data/

# update the default file
sudo tee /etc/nginx/sites-available/default > /dev/null <<EOF
server {
        listen 80 default_server;
        error_page 404 /404.html;
        location = /404.html {
                root /var/www/html;
                internal;
        }
        listen [::]:80 default_server;

        location /hbnb_static {
                 alias /data/web_static/current/;
        }

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;
        rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;

        
        location / {
        # Added by me
        add_header X-Served-By $hostname;
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files $uri $uri/ =404;
        }
}
EOF
# restart nginx
sudo service nginx restart