#!/usr/bin/python3

import gizeh
import moviepy.editor as edit
import argparse

W, H = 128, 128

# The sensor data, where each time t is mapped
# to the sensor value at that instant
sensor_data = {}

def make_frame(t):

    surface = gizeh.Surface(W,H, bg_color=(0, 0, 0, 0))
    radius = W * (1 + (t * (2 - t)) ** 2 ) / 6
    circle = gizeh.circle(radius, xy = (W / 2,H / 2), fill=(1, 0, 0))
    circle.draw(surface)
    return surface.get_npimage()


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

    clip1 = edit.VideoFileClip("./example-video/EXAMPLE1.MOV")
    graphics = edit.VideoClip(make_frame, duration=clip1.duration)
    # clip2 = edit.VideoFileClip("./example-video/EXAMPLE2.MOV")
    # final = edit.concatenate_videoclips([clip1, clip2])

    write_file(edit.CompositeVideoClip([clip1, graphics.set_position((100, 100))]), "out/out.mp4")

if __name__ == "__main__":
    main()


