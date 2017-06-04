#ifndef COMMUNICATION_H
#define COMMUNICATION_H 

#include <stddef.h>
#include <stdint.h>

const int ADDRESS = 0x66;

void communication_setup();

void on_request();

void update();

#endif /* ifndef COMMUNICATION_H */
