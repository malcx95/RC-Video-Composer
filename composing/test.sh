#!/bin/bash
./main.py \
    --maincam ../recordings/20170823-114142/video.mp4 \
    --seccam example-video/EXAMPLE2.MOV \
    --sensordata ../recordings/20170823-114142/sensor.csv \
    --reverse \
    --output $1
