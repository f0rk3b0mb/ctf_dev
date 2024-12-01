#!/bin/bash

<<<<<<< HEAD
docker build -t web_consolidation_1 .

docker run --rm --name web_consolidation -p 8080:8080 -dit web_consolidation_1
=======
docker kill web_consolidation

docker build -t web_consolidation .

docker run --rm -p 10011:1234  -it web_consolidation
>>>>>>> a49e69fe83a7b6256fc7ae3c1398e74cf77d23fc
