#include "speed.h"
#include <Arduino.h>

/*
 * The current speed in km/h
 */
volatile uint8_t speed;
volatile float rpm;
volatile unsigned long previous_time;

void speed_setup() {
    pinMode(HALL_SENSOR_PIN, INPUT);
    speed = 0;
    rpm = 0.0;
    attachInterrupt(digitalPinToInterrupt(HALL_SENSOR_PIN), on_magnet_flip, RISING);
}

void on_magnet_flip() {
    unsigned long prev = previous_time;
    previous_time = micros();

    speed = (uint8_t)((METERS_PER_TURN / 
            (float)(previous_time - prev)) * CONVERSION_FACTOR_TO_KMH);

    rpm = MINUTE_IN_MICROSECONDS / ((float)(previous_time - prev));
}

float get_rpm() {
    return rpm;
}

uint8_t get_speed() {
    return speed;
}


