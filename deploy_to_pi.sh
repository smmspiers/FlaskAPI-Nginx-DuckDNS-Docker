#!/bin/bash

echo "Copying app to pi"
scp -r /Users/Sammy/Documents/Projects/flask_nginx_docker pi@192.168.0.31:/var/www

echo "Restarting docker"
ssh pi@192.168.0.31 << 'ENDSSH'
  cd /var/www/flask_nginx_docker
  bash run_app_in_docker.sh
ENDSSH