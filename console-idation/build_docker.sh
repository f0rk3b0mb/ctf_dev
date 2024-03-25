#!/bin/bash

docker build -t web_consolidation .

docker run --rm -p 80:80  -it web_consolidation