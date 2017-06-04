#include "pwmread.h"
#include "speed.h"
#include "communication.h"

PWM_STATUS status;

int i;

void setup() {

    pinMode(13, OUTPUT);

    Serial.begin(9600);

    speed_setup();

    pwm_read_setup(22, &status);

    communication_setup();

}

void loop() {

    i++;

    update();
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

