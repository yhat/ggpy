#!/bin/bash

python generate-examples-html.py examples > index.html

for f in docs/*/*.ipynb
do
  DIR=$(dirname "${f}")
  mkdir -p "${DIR}"
  FILENAME=$(basename "${f}")
  jupyter nbconvert "${f}" --stdout > "./build/${DIR}/${FILENAME}"
done
