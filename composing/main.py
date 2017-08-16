#!/usr/bin/python3

import gizeh
import moviepy.editor as edit
import argparse
import numpy
import scipy
import pdb
import math

W, H = 128, 128

# The sensor data, where each time t is mapped
# to the sensor values at that instant
global sensor_data

global main_clip
global steering_image
global throttle_image

STEERING_POS = (100, 100)
THROTTLE_POS = (1700, 100)
PADDING = 3

def make_steering_frame(t):

    global main_clip
    global steering_image
    global sensor_data

    width = len(steering_image[0])
    height = len(steering_image)

    return key_out_color(steering_image, 
                         main_clip.get_frame(t),
                         make_steering_mask_frame(t, sensor_data, 
                                                  width, height),
                         STEERING_POS, width, height)


def make_throttle_frame(t):

    global main_clip
    global throttle_image
    global sensor_data

    width = len(throttle_image[0])
    height = len(throttle_image)

    return key_out_color(throttle_image, 
                         main_clip.get_frame(t),
                         make_throttle_mask_frame(t, sensor_data,
                                                  width, height),
                         THROTTLE_POS, width, height)


def key_out_color(foreground, background, mask, pos, width, height):
    """Makes the given color transparent in the foreground frame"""

    # Create a result image
    result = [[(0, 0, 0) for x in range(width)] for y in range(height)]

    x_pos, y_pos = pos

    for x in range(width):
        for y in range(height):
            y_index = y + y_pos
            x_index = x + x_pos
            if mask[y][x]:
                result[y][x] = background[y_index][x_index]
            else:
                result[y][x] = foreground[y][x]
    return numpy.array(result)



def read_sensor_data(sensor_file, main_clip):
    lines = None
    with open(sensor_file) as f:
        lines = f.readlines()
    date = lines[0]
    raw_sensor_data = lines[1:]

    result = {}

    data_index = 0

    last_value = None

    # iterate over the times
    for time, _ in main_clip.iter_frames(with_times=True, fps=25):
        while True:
            if data_index == len(raw_sensor_data):
                # in case the sensor data ended before the video did
                result[time] = last_value
                break

            d = raw_sensor_data[data_index].split(',')
            _, _, _, elapsed = d

            if float(elapsed) >= time:
                value = process_sensor_data(d)
                result[time] = value
                last_value = value
                break
            data_index += 1
    return result


def process_sensor_data(raw_data):
    """
    Creates one sensor data frame from the given raw data
    frame. The result is ready to be read by the video 
    processing functions.

    Returns (speed (km/h), steering (-50 to 50), throttle (-50 to 50))
    """
    speed, steering, throttle, _ = raw_data
    return (int(speed), int((int(steering) - 127) * (50.0 / 127.0)),
           int((int(throttle) - 127) * (50.0 / 127.0)))
 

def make_steering_mask_frame(t, sensor_data, width, height):
    _, steering, _ = sensor_data[t]
    return create_steering_mask(steering, width, height)


def make_throttle_mask_frame(t, sensor_data, width, height):
    _, _, throttle = sensor_data[t]
    return create_throttle_mask(throttle, width, height)


def create_throttle_mask(throttle, width, height):
    """
    Creates a mask for masking out the throttle scale.

    throttle must be a value from -20 (100% brake) to 50 (100% throttle)
    """

    num_ticks = abs(throttle)

    tick_height = height // 70

    result = [[True for x in range(width)] for y in range(height)]

    if (throttle >= 0):
        # throttle
        for tick in range(num_ticks):
            tick_index = tick * tick_height + (height // 10) * 2
            for i in range(tick_height - PADDING):
                result[tick_index + i] = [False for x in range(width)]
    else:
        # braking
        for tick in range(num_ticks):
            tick_index = (height // 10) * 2 - tick * tick_height
            for i in range(tick_height - PADDING):
                result[tick_index - i - 1] = [False for x in range(width)] 
    return result


def create_steering_mask(steering, width, height):
    """
    Creates a mask for masking out the steering scale.

    steering must be a value from -50 (100% left) to 50 (100% right)
    """

    num_ticks = abs(steering)

    tick_width = width // 100

    row = [True for x in range(width)]

    if (steering >= 0):
        # steering to the right
        for tick in range(num_ticks):
            tick_index = tick * tick_width + width // 2
            for i in range(tick_width - PADDING):
                row[tick_index + i] = False
    else:
        # steering to the left
        for tick in range(num_ticks):
            tick_index = width // 2 - tick * tick_width
            for i in range(tick_width - PADDING):
                row[tick_index - i - 1] = False 
    return [row for y in range(height)]


def color_equals(c1, c2):
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    return r1 == r2 and g1 == g2 and b1 == b2


def write_file(clip, output_file):
    clip.write_videofile(output_file)
    

def main():
    argparser = argparse.ArgumentParser(description=
                            "Produce video from raw footage and sensor data.")

    argparser.add_argument("--maincam", type=str, 
                           help="The footage from the front facing camera.",
                           required=True)

    argparser.add_argument("--seccam", type=str, 
                           help="The footage from the secondary camera.",
                           required=True)

    argparser.add_argument("--sensordata", type=str, 
                           help="The sensor data file.", required=True)

    argparser.add_argument("--output", type=str, help="Output file name",
                          default="out.mp4")

    args = argparser.parse_args()

    global main_clip
    main_clip = edit.VideoFileClip(args.maincam)

    global sensor_data
    sensor_data = read_sensor_data(args.sensordata, main_clip)

    global steering_image
    steering_image = scipy.ndimage.imread("graphics/steering-background.png")
    
    global throttle_image
    throttle_image = scipy.ndimage.imread("graphics/throttle-background.png")

    steering_graphics = edit.VideoClip(make_steering_frame, duration=main_clip.duration)

    throttle_graphics = edit.VideoClip(make_throttle_frame, 
                                       duration=main_clip.duration)
    # clip2 = edit.VideoFileClip("./example-video/EXAMPLE2.MOV")
    # final = edit.concatenate_videoclips([clip1, clip2])

    write_file(
        edit.CompositeVideoClip([
            main_clip, steering_graphics.set_position(STEERING_POS),
            throttle_graphics.set_position(THROTTLE_POS)]),
               args.output)

if __name__ == "__main__":
    main()


