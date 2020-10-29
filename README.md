# docker-tutorial - commands


#docker commit layer:
$docker run -tid --name py python

$docker ps

$docker exec -it py bash

$touch first.txt

$echo >> first.txt how are you?

$exit

$docker container commit py  python:first
