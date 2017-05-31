#include "speed.h"
#include <Arduino.h>

volatile float rpm;
volatile unsigned long previous_time;

void speed_setup() {
    pinMode(HALL_SENSOR_PIN, INPUT);
    attachInterrupt(digitalPinToInterrupt(HALL_SENSOR_PIN), on_magnet_flip, RISING);
}

void on_magnet_flip() {
    unsigned long prev = previous_time;
    previous_time = micros();

    rpm = MINUTE_IN_MICROSECONDS / ((float)(previous_time - prev));
}

float get_rpm() {
    return rpm;
}

