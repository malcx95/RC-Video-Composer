#!/usr/bin/python3

import smbus

def i2c_test():
    bus = smbus.SMBus(1)
    # bus.write_block_data(0x66, 0, [2, 32, 1, 0, 23])
    print(bus.read_i2c_block_data(0x66, 0, 10))
    bus.close()


def main():
    i2c_test()


if __name__ == "__main__":
    main()

