#include "pwmread.h"
#include <Arduino.h>

void pwm_read_setup(uint8_t pin, PWM_STATUS* status) {
    pinMode(pin, INPUT);
    status->pulse_width = 0;
    status->pulse_start_time= 0;
    status->is_high = false;
}


void update_pwm(uint8_t pin, PWM_STATUS* status) {
    if (digitalRead(pin) == LOW) {
        // if the input already was high, don't do anything
        if (status->is_high) {
            return;
        }
        // the edge is rising, start timing.
        status->pulse_start_time = micros();
        status->is_high = true;
    } else {
        // if the input was already low, don't do anything
        if (!status->is_high) {
            return;
        }
        // the edge is falling, stop timing
        status->pulse_width = micros() - status->pulse_start_time;
        status->is_high = false;
    }
}

