#!/bin/bash

rm *.pyc
scp -r ./* pi@zero:/home/pi/RC-Video-Composer/pi

if [ $? -ne 0 ]; then
    echo "Upload failed"
    exit 1
fi

