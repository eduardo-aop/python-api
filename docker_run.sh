#!/bin/bash

echo 'docker image building ....'
docker build -t python-api-image .
echo 'docker image build'

docker-compose up --build -d

echo 'docker image run....'
docker run -p 5000:5000 python-api-image