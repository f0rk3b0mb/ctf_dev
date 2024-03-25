#!/bin/bash

docker build -t web_template .

docker run --rm -p 80:80  -it web_template