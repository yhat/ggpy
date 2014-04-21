#!/bin/bash

for f in `find ./ggplot/tests/baseline_images | grep .png$`
do
  f2=`basename $f`
  newf=`find result_images | grep "$f2"`
  echo $newf
  mv -f $newf $f
done

