#ifndef PWM_READ_H
#define PWM_READ_H 

#include <stdbool.h>
#include <stdint.h>

typedef struct {

    unsigned long pulse_width;
    unsigned long pulse_start_time;
    bool is_high;

} PWM_STATUS;

void pwm_read_setup(uint8_t pin, PWM_STATUS* status);

void update_pwm(uint8_t pin, PWM_STATUS* status);

#endif /* ifndef PWM_READ_H */

