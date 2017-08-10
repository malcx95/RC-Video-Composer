#!/usr/bin/python3

import gizeh
import moviepy.editor as edit
import argparse
import numpy
import pdb

W, H = 128, 128

# The sensor data, where each time t is mapped
# to the sensor value at that instant
sensor_data = {}

GRAPHICS_POS = (100, 100)

global main_clip

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
    graphics = edit.VideoClip(make_frame, duration=main_clip.duration)
    # clip2 = edit.VideoFileClip("./example-video/EXAMPLE2.MOV")
    # final = edit.concatenate_videoclips([clip1, clip2])

    write_file(edit.CompositeVideoClip([main_clip,
                                        graphics.set_position(GRAPHICS_POS)]),
               "out/out1.mp4")

if __name__ == "__main__":
    main()


