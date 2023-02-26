#!/bin/bash
HASH=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 4 | head -n 1)
name=${USER}_annotated_s4_GPU__${HASH}

echo "Launching container named '${name}'"
# Launches a docker container using our image, and runs the provided command

docker run -d --rm \
    --runtime=nvidia \
    --gpus "device=$CUDA_VISIBLE_DEVICES" \
    --name $name \
    --user 1001 \
    -v `pwd`:/home/duser/entryfolder \
    -e PYTHONPATH=/home/duser/entryfolder \
    -t annotated_s4 \
    ${@:1}
