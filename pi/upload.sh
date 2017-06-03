#!/bin/bash

rm *.pyc
scp -r ./* pi@zero:/home/pi/RaspPiAlarmclock/src

if [ $? -ne 0 ]; then
    echo "Upload failed"
    exit 1
fi
