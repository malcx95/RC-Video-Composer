# RC Video Composer

This project involves putting a Raspberry PI Zero on a 1:8th scale R/C
nitro powered buggy. This Raspberry PI records video while collecting sensor
data from a Teensy LC, which records the speed of the car the throttle and steering servo positions. The video and
sensor data are then fed through a python script which composes the data
into a video with the sensor data visualised.

![alt text](https://github.com/malcx95/RC-Video-Composer/blob/master/schematic/schematic.png)

I finished programming the Raspberry Pi and the Teensy and got everything to work. However when test driving
the actual car, the Pi kept dying whenever I hit something, so no recordings survived. Also the
magnets on the driveshaft and the sensor I was using to record speed were lost during driving.

