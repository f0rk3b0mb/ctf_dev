#!/bin/bash

docker kill web_template

docker build -t web_template .

docker run --rm -p 10010:1235  -it web_template
