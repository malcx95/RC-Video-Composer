#include "speed.h"

void setup() {

    pinMode(23, INPUT_PULLUP);
    pinMode(13, OUTPUT);

    Serial.begin(9600);

    speed_setup();

}

void loop() {

    if (digitalRead(23) == HIGH) {
        digitalWrite(13, HIGH);
    } else {
        digitalWrite(13, LOW);
    }

    Serial.println(get_rpm());

    delay(100);
}

