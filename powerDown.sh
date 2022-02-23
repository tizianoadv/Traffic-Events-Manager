#!/bin/bash

#Buffer
docker exec buffer /bin/bash -c "echo Buffer"
docker exec buffer /bin/bash -c "service mosquitto stop"
docker exec buffer /bin/bash -c "service rabbitmq-server stop"

#Database
docker exec database /bin/bash -c "echo Database"
docker exec database /bin/bash -c "service redis-server stop"

#Webserver
docker exec webserver /bin/bash -c "echo Webserver"
docker exec webserver /bin/bash -c "service mosquitto stop"

#Eventhub
docker exec eventhub /bin/bash -c "echo Eventhub"
docker exec eventhub /bin/bash -c "service mosquitto stop"

#Gateway
docker exec gateway /bin/bash -c "echo Gateway"
docker exec gateway /bin/bash -c "service mosquitto stop"

#Docker containers
docker stop dhcp gateway eventhub buffer database webserver

#Vehicles
lxc-stop -n vehicles