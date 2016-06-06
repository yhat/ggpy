#!/bin/bash

python generate-examples-html.py examples > index.html

for f in docs/*/*.ipynb
do
  DIR=$(dirname "${f}")
  mkdir -p "./build/${DIR}"
  FILENAME=$(basename "${f}")
  FILENAME="${FILENAME/.ipynb/.html}"
  jupyter nbconvert "${f}" --stdout > "./build/${DIR}/${FILENAME}"
done
