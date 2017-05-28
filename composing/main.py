#!/usr/bin/python3

import gizeh
import moviepy.editor as edit

W, H = 128, 128

def make_frame(t):
   surface = gizeh.Surface(W,H, bg_color=None)
   radius = W * (1 + (t * (2 - t)) ** 2 ) / 6
   circle = gizeh.circle(radius, xy = (W / 2,H / 2), fill=(1, 0, 0))
   circle.draw(surface)
   return surface.get_npimage()


def write_file(clip, output_file):
    clip.write_videofile(output_file)
    

def main():
    clip1 = edit.VideoFileClip("./example-video/EXAMPLE1.MOV")
    graphics = edit.VideoClip(make_frame, duration=clip1.duration)
    # clip2 = edit.VideoFileClip("./example-video/EXAMPLE2.MOV")
    # final = edit.concatenate_videoclips([clip1, clip2])

    write_file(edit.CompositeVideoClip([clip1, graphics.set_position((100, 100))]), "out/out.mp4")

if __name__ == "__main__":
    main()

