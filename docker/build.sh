#!/bin/bash

echo 'Building Dockerfile with image name annotated_s4'
# docker build --no-cache --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g)  -t annotated_s4 .
docker build --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g)  -t annotated_s4 .
