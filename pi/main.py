#!/usr/bin/python3

from datetime import datetime
import time
import smbus

SENSOR_DATA_FORMAT = "Speed: {} km/h\nSteering: {}\nThrottle: {}\nTemperature: {} C"

class SensorDataFrame:

    def __init__(self, data):
        self.speed, self.steering, self.throttle, self.temp = data
        self.timestamp = datetime.now()

    def __str__(self):
        return SENSOR_DATA_FORMAT.format(self.speed, self.steering, 
                                         self.throttle, self.temp)


def i2c_test():
    bus = smbus.SMBus(1)
    # bus.write_block_data(0x66, 0, [2, 32, 1, 0, 23])
    try:
        while True:
            start = time.time()
            try:
                data = bus.read_i2c_block_data(0x66, 0, 4)
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
    i2c_test()


if __name__ == "__main__":
    main()

