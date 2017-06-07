#ifndef SPEED_H
#define SPEED_H 

#include <stdint.h>

const uint8_t HALL_SENSOR_PIN = 23;
const float CONVERSION_FACTOR_TO_KMH = 3.6 * 1.0e6;
const float MINUTE_IN_MICROSECONDS = 60000000.0;
const float METERS_PER_TURN = 0.101;

void speed_setup();

void on_magnet_flip();

float get_rpm();

uint8_t get_speed();

#endif /* ifndef SPEED_H */

