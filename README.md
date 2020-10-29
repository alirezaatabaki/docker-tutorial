# docker-tutorial - commands
#Port forwarding
-p 8080:80 ==> IP = 0.0.0.0

#Save/Load
$docker save -o ap.tar alpine:latest

#docker commit layer:
$docker run -tid --name py python

$docker ps

$docker exec -it py bash

$touch first.txt

$echo >> first.txt how are you?

$exit

$docker container commit py  python:first
