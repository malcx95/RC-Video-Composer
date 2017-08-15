#!/usr/bin/python3

import gizeh
import moviepy.editor as edit
import argparse
import numpy
import pdb
import math

W, H = 128, 128

# The sensor data, where each time t is mapped
# to the sensor values at that instant
global sensor_data

global main_clip

GRAPHICS_POS = (100, 100)
PADDING = 3

def make_frame(t):

    global main_clip
    # width, height = main_clip.size

    surface = gizeh.Surface(W, H, bg_color=(0, 0, 0))
    radius = W * (1 + (t * (2 - t)) ** 2 ) / 6
    circle = gizeh.circle(radius, xy = (W / 2,H / 2), fill=(1, 0, 0))
    circle.draw(surface)

    return key_out_color(surface.get_npimage(), 
                         main_clip.get_frame(t), (0, 0, 0), 
                         W, H, GRAPHICS_POS)


def read_sensor_data(sensor_file, main_clip):
    lines = None
    with open(sensor_file) as f:
        lines = f.readlines()
    date = lines[0]
    raw_sensor_data = lines[1:]

    result = {}

    data_index = 0

    # iterate over the times
    for time, _ in main_clip.iter_frames(with_times=True):
        while True:
            if data_index == len(raw_sensor_data):
                break
            d = raw_sensor_data[data_index].split(',')
            _, _, _, elapsed = d
            if float(elapsed) >= time:
                result[time] = process_sensor_data(d)
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
 

def create_steering_mask(steering, width, height):
    """
    Creates a mask for masking out the steering scale.

    steering must be a value from -50 (100% left) to 50 (100% right)
    """

    num_ticks = abs(steering)

    tick_width = width // 100

    row = [0.0 for x in range(width)]

    if (steering >= 0):
        # steering to the right
        for tick in range(num_ticks):
            tick_index = tick * tick_width + width // 2
            for i in range(tick_width - PADDING):
                row[tick_index + i] = 1.0
    else:
        # steering to the left
        for tick in range(num_ticks):
            tick_index = width // 2 - tick * tick_width
            for i in range(tick_width - PADDING):
                row[tick_index - i - 1] = 1.0
    return [row for y in range(height)]


def color_equals(c1, c2):
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    return r1 == r2 and g1 == g2 and b1 == b2


def key_out_color(foreground, background, color, width, height, pos):
    """Makes the given color transparent in the foreground frame"""

    # Create a result image
    result = [[(0, 0, 0) for x in range(width)] for y in range(height)]

    x_pos, y_pos = pos


    for x in range(width):
        for y in range(height):
            y_index = y + y_pos
            x_index = x + x_pos
            if color_equals(foreground[x][y], color):
                result[y][x] = background[y_index][x_index]
            else:
                result[y][x] = foreground[y][x]
    return numpy.array(result)


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

    args = argparser.parse_args()

    global main_clip
    main_clip = edit.VideoFileClip(args.maincam)

    global sensor_data
    sensor_data = read_sensor_data(args.sensordata, main_clip)

    for t, _ in main_clip.iter_frames(with_times=True):
        print(str(t) + ":" + " " + str(sensor_data[t]))

    # pdb.set_trace()

    graphics = edit.VideoClip(make_frame, duration=main_clip.duration)
    # clip2 = edit.VideoFileClip("./example-video/EXAMPLE2.MOV")
    # final = edit.concatenate_videoclips([clip1, clip2])

    write_file(edit.CompositeVideoClip([main_clip,
                                        graphics.set_position(GRAPHICS_POS)]),
               "out/out1.mp4")

if __name__ == "__main__":
    main()


