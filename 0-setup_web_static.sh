#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.
FAKE_HTML="<html>\n  <head>\n  </head>\n  <body>\n\tHolberton School\n  </body>\n</html>"
SERVER_BLOCK_PATH="/etc/nginx/sites-available/default"
ROOT_DIR="/data"
RELEASE="$ROOT_DIR/web_static/releases/test"
SHARE="$ROOT_DIR/web_static/shared"
LINK="$ROOT_DIR/web_static/current"
STATIC="\n\tlocation /hbnb_static/ {\n\t\talias $LINK/;\n\t}\n"

# update and install NGINX if not available
sudo apt-get update && sudo apt-get -y install nginx

# create the directory to hold the web page
sudo mkdir -p "$RELEASE" "$SHARE"

# add the HTML in the required file
echo -e "$FAKE_HTML" | sudo tee "$RELEASE/index.html"

# create a symbolic link between two file system paths
sudo ln -sf "$RELEASE" "$LINK"

# change ownership to ubuntu
sudo chown -hR ubuntu:ubuntu "$ROOT_DIR"

# modify the code at a specific line number using an alias
sudo sed -i "46 a\ $STATIC" "$SERVER_BLOCK_PATH"

# restart nginx server
sudo service nginx restart
