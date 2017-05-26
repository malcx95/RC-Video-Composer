#!/usr/bin/python3

import moviepy.editor as edit

def main():
    clip1 = edit.VideoFileClip("./example-video/EXAMPLE1.MOV")
    clip2 = edit.VideoFileClip("./example-video/EXAMPLE2.MOV")
    final = edit.concatenate_videoclips([clip1, clip2])
    final.write_videofile("out/out.mp4")

if __name__ == "__main__":
    main()

