#include "communication.h"
#include <i2c_t3.h>
#include <Arduino.h>
#include <stdbool.h>

volatile bool available;
uint8_t buffer[10] = {19, 1, 2, 4, 5, 6, 7, 8, 9, 10};

void communication_setup() {
    Wire.begin(I2C_SLAVE, 0x66, I2C_PINS_18_19, I2C_PULLUP_EXT, 100000);
    Wire.onRequest(on_request);
    available = false;
}

void update() {
    if (available) {
        for (int i = 0; i < 10; ++i) {
            Serial.print(buffer[i]);
            Serial.print(' ');
        }
        Serial.println(" ");
    }
    available = false;
}

void on_request() {
    Wire.write(buffer, 10);
    digitalWrite(13, LOW);
    available = true;
}

