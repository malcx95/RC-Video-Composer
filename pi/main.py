#!/usr/bin/python3

from datetime import datetime
import time
import smbus
import os

OUTPUT_DIR = "/home/pi/recordings"

SENSOR_UNIT_ADDRESS = 0x66
SENSOR_DATA_LENGTH = 3
SENSOR_DATA_PRINT_FORMAT = "Speed: {} km/h\nSteering: {}\nThrottle: {}"
SENSOR_DATA_FILE_FORMAT = "{speed},{steering},{throttle},{elapsed}"

class SensorDataFrame:

    def __init__(self, data):
        self.speed, self.steering, self.throttle = data
        self.timestamp = datetime.now()

    def __str__(self):
        return SENSOR_DATA_PRINT_FORMAT.format(self.speed, self.steering, 
                                         self.throttle)


def setup():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


def should_cancel():
    """
    Returns whether someone presses the cancel button.
    """

    # TODO implement
    return False


def record():
    recording_dir = os.path.join(
        OUTPUT_DIR,
        datetime.now().strftime("%Y%m%d%-%H%M%S"))
    os.makedirs(recording_dir)

    # TODO start video recording
    
    with open(os.path.join(recording_dir, "sensor.csv")) as output:
        # write the start of the recording
        start_datetime = datetime.now()
        output.write(start_datetime.strftime("%Y,%m,%d,%H,%M,%S,%f") + '\n')
        start_time = time.time()

        while not should_cancel():
            try:
                speed, steering, throttle = bus.read_i2c_block_data(
                    SENSOR_UNIT_ADDRESS, 0, SENSOR_DATA_LENGTH)
                output.write(SENSOR_DATA_PRINT_FORMAT.format(
                    speed=speed, steering=steering, throttle=throttle, 
                        elapsed=str(time.time() - start_time)))
                
            except (IOError, TimeoutError, OSError):
                pass
            time.sleep(0.028)


def i2c_test():
    bus = smbus.SMBus(1)
    # bus.write_block_data(0x66, 0, [2, 32, 1, 0, 23])
    try:
        while True:
            start = time.time()
            try:
                data = bus.read_i2c_block_data(SENSOR_UNIT_ADDRESS,
                                               0, SENSOR_DATA_LENGTH)
                print(str(SensorDataFrame(data)))
            except (IOError, TimeoutError, OSError):
                pass
            time.sleep(0.028)
            print("")
            print("Time: " + str(time.time() - start))
            print("")
    except KeyboardInterrupt:
        pass
    finally:
        bus.close()


def main():
    setup()
    # i2c_test()
    


if __name__ == "__main__":
    main()

