#!/bin/bash


#docker volume rm $(docker volume ls | awk {'print $2'})


docker rm -f $(docker ps -qa)