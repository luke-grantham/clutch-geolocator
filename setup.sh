#!/bin/sh

if [ $# -ne 1 ]; then
    echo Error: you must supply the api key as an argument
    echo API key was sent seperatly through email
    exit 1
fi

api_key=$1

docker build -t geolocator-db ./geolocator-db
docker build -t geolocator-server ./geolocator-server
docker run -d -p 5432:5432 geolocator-db
docker run -d -p 5000:5000 geolocator-server ${api_key}
