#ifndef SPEED_H
#define SPEED_H 

#include <stdint.h>

const uint8_t HALL_SENSOR_PIN = 23;
const float MINUTE_IN_MICROSECONDS = 60000000.0;

void speed_setup();

void on_magnet_flip();

float get_rpm();

#endif /* ifndef SPEED_H */

