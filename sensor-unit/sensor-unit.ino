#include "pwmread.h"
#include "speed.h"
#include <stddef.h>
#include <stdint.h>
#include <i2c_t3.h>

PWMStatus throttle;
PWMStatus steering;
const int I2C_ADDRESS = 0x66;

void setup() {

    pinMode(13, OUTPUT);

    Serial.begin(9600);

    speed_setup();

    pwm_read_setup(22, &throttle, 0);

    communication_setup();

}

void loop() {

    // if (digitalRead(23) == HIGH) {
    //     digitalWrite(13, HIGH);
    // } else {
    //     digitalWrite(13, LOW);
    // }

    // update_pwm(22, &status);

    // if (i % 1000 == 0) {
    //     Serial.println(status.pulse_width - 8000);
    // }

    // Serial.println(get_rpm());

    // delay(100);
}

void communication_setup() {
    Wire.begin(I2C_SLAVE, I2C_ADDRESS, I2C_PINS_18_19, I2C_PULLUP_EXT, 100000);
    Wire.onRequest(on_request);
    Wire.onReceive(on_command);
}

void update() {
    // if (available) {
    //     for (int i = 0; i < 10; ++i) {
    //         Serial.print(buffer[i]);
    //         Serial.print(' ');
    //     }
    //     Serial.println(" ");
    // }
    // available = false;
}

void on_request() {
    // Wire.write(buffer, 10);
    // digitalWrite(13, LOW);
    // available = true;
}

void on_command(size_t num_bytes) {
    
}

