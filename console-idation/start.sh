#!/bin/sh

#secure start
chmod  600 /start.sh

mv /flag.txt /flag$(cat /dev/urandom | tr -cd "a-f0-9" | head -c 10).txt

# Start Nginx in the background
nginx -g "daemon off;" &

# Start your Flask app
python /app/main.py
