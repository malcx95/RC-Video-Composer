#include "pwmread.h"
#include "speed.h"
#include "temp.h"
#include <stddef.h>
#include <stdint.h>
#include <i2c_t3.h>

const int I2C_ADDRESS = 0x66;
const int I2C_FREQ = 10000;
const int MESSAGE_LENGTH = 4;

PWMStatus throttle;
PWMStatus steering;
int temperature;

int i;

void setup() {

    pinMode(13, OUTPUT);

    Serial.begin(9600);

    speed_setup();

    pwm_read_setup(16, &throttle, 0);
    pwm_read_setup(15, &steering, 0);

    communication_setup();

    i = 0;

}

void loop() {

    i++;

    update_pwm(22, &throttle);

    if (i % 50000 == 0) {
        Serial.println(get_current_value(&throttle));
    }

}

void communication_setup() {
    Wire.begin(I2C_SLAVE, I2C_ADDRESS, I2C_PINS_18_19,
               I2C_PULLUP_EXT, I2C_FREQ);
    Wire.onRequest(on_request);
    Wire.onReceive(on_command);
}

void on_request() {
    digitalWrite(13, HIGH);
    uint8_t message[MESSAGE_LENGTH];
    message[0] = get_speed();
    message[1] = 12;
    message[2] = get_current_value(&throttle);
    message[3] = 70;
    Wire.write(message, MESSAGE_LENGTH);
    digitalWrite(13, LOW);
}

void on_command(size_t num_bytes) {
    
}

