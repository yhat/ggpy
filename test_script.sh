#!/bin/bash

test ! -f /tmp/GGPLOT-CHECKSUMS && touch /tmp/GGPLOT-CHECKSUMS

find ggplot -name '*.py' | xargs md5 > /tmp/GGPLOT-CHECKSUMS-NEW
if ! diff /tmp/GGPLOT-CHECKSUMS /tmp/GGPLOT-CHECKSUMS-NEW; then
  find ggplot -name '*.py' | xargs md5 > /tmp/GGPLOT-CHECKSUMS
  python setup.py install > /dev/null
fi

export GGPLOT_DEV="1"
python $1
