#!/bin/bash

if [[ "$(diff ./requirements.txt ./.requirements.txt)" != "" ]]; then
  echo "...Installing new packages.."
  docker build -t jupyter_lab .
  cp requirements.txt .requirements.txt 
fi

docker run --rm --name=jupyter_lab \
  -v "$PWD":/workdir \
  -w /workdir \
  -p 8888:8888 \
  -e JUPYTER_ENABLE_LAB=yes \
  -e NB_USER=enrique \
  jupyter_lab
  
