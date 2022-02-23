#!/bin/bash

#DHCP
docker run -it --rm --init --net host -v "$(pwd)/data":/data networkboot/dhcpd br0

#Vehicles
lxc-start -n vehicles

#Docker containers
docker start gateway eventhub buffer database webserver

#Gateway
docker exec gateway /bin/bash -c "echo Gateway"
docker exec gateway /bin/bash -c "service mosquitto start"

#Eventhub
docker exec eventhub /bin/bash -c "echo Eventhub"
docker exec eventhub /bin/bash -c "service mosquitto start"

#Webserver
docker exec webserver /bin/bash -c "echo Webserver"
docker exec webserver /bin/bash -c "service mosquitto start"

#Database
docker exec database /bin/bash -c "echo Database"
docker exec database /bin/bash -c "service redis-server start"

#Buffer
docker exec buffer /bin/bash -c "echo Buffer"
docker exec buffer /bin/bash -c "service mosquitto start"
docker exec buffer /bin/bash -c "service rabbitmq-server start"


