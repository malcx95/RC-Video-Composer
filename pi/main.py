#!/usr/bin/python3

from datetime import datetime
import RPi.GPIO as GPIO
import time
import smbus
import os
import picamera

OUTPUT_DIR = "/home/pi/recordings"

SENSOR_UNIT_ADDRESS = 0x66
SENSOR_DATA_LENGTH = 3
SENSOR_DATA_PRINT_FORMAT = "Speed: {} km/h\nSteering: {}\nThrottle: {}"
SENSOR_DATA_FILE_FORMAT = "{speed},{steering},{throttle},{elapsed}"

LED_GREEN = 26
LED_YELLOW1 = 19

# This LED doesn't work :(
# LED_YELLOW2 = 20

LED_YELLOW2 = 17
LED_RED = 14
BUTTON_PORT = 21


def setup_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


def button_pressed():
    """
    Returns whether someone is pressing the button.
    """
    return not GPIO.input(BUTTON_PORT)


def record(camera):

    recording_dir = os.path.join(
        OUTPUT_DIR,
        datetime.now().strftime("%Y%m%d-%H%M%S"))
    os.makedirs(recording_dir)

    sensor_values = {}

    bus = smbus.SMBus(1)
    
    start_datetime = datetime.now()

    camera.start_recording(os.path.join(recording_dir, "video.h264"))
    start_time = time.time()

    while not button_pressed():
        try:
            speed, steering, throttle = bus.read_i2c_block_data(
                SENSOR_UNIT_ADDRESS, 0, SENSOR_DATA_LENGTH)

            sensor_values[time.time() - start_time] = (speed, 
                                                       steering,
                                                       throttle)

        except (IOError, TimeoutError, OSError):
            continue
        time.sleep(0.02)
    camera.stop_recording()

    with open(os.path.join(recording_dir, "sensor.csv"), 'w') as output:
        output.write(start_datetime.strftime("%Y,%m,%d,%H,%M,%S,%f"))
        for t in sorted(sensor_values.keys()):
            speed, steering, throttle = sensor_values[t]
            data_packet = SENSOR_DATA_FILE_FORMAT.format(
                speed=speed, steering=steering, throttle=throttle, 
                    elapsed=t)
            output.write(data_packet + '\n')


def i2c_test():
    bus = smbus.SMBus(1)
    # bus.write_block_data(0x66, 0, [2, 32, 1, 0, 23])
    try:
        while not button_pressed():
            start = time.time()
            try:
                data = bus.read_i2c_block_data(SENSOR_UNIT_ADDRESS,
                                               0, SENSOR_DATA_LENGTH)
                print(data)
            except (IOError, TimeoutError, OSError):
                pass
            time.sleep(0.02)
            print("")
            print("Time: " + str(time.time() - start))
            print("")
    except KeyboardInterrupt:
        pass
    finally:
        bus.close()


def countdown():
    """
    Blinks the green and yellow leds three times. 
    Cancels if button is pressed. Returns False if cancelled,
    True otherwise.
    """

    GPIO.output(LED_GREEN, False)

    time.sleep(1)

    for led in [LED_GREEN, LED_YELLOW1, LED_YELLOW2]:
        for i in range(6):
            time.sleep(0.5)

            if button_pressed():
                GPIO.output(led, False)
                return False

            GPIO.output(led, (i + 1) % 2)

    time.sleep(0.5)
    return True


def main():

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(LED_RED, GPIO.OUT)
    GPIO.setup(LED_GREEN, GPIO.OUT)
    GPIO.setup(LED_YELLOW1, GPIO.OUT)
    GPIO.setup(LED_YELLOW2, GPIO.OUT)

    GPIO.setup(BUTTON_PORT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    setup_output_dir()

    with picamera.PiCamera(resolution="1920x1080", framerate=25) as camera:

        while True:

            # Standby mode

            GPIO.output(LED_GREEN, True)
            GPIO.output(LED_RED, False)

            if button_pressed():
                if countdown():
                    GPIO.output(LED_RED, True)
                    record(camera)
                    GPIO.output(LED_RED, False)
                    time.sleep(1)

            time.sleep(0.1)


    # setup()
    # record()
    # i2c_test()
    # camera = picamera.PiCamera()
    # try:
    #     camera.start_recording('test.h264')
    #     while True:
    #         time.sleep(1)
    # except KeyboardInterrupt:
    #     camera.stop_recording()


if __name__ == "__main__":
    try:
        main()
    finally:
        GPIO.cleanup()

