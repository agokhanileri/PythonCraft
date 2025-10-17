#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AGI, 2025Sep, Strachnotes
"""

# Image Conversion
import pillow_jxl  # activates JXL support
from pathlib import Path  # 
import magic
from PIL import Image
import pillow_heif

path_in = Path("/Users/agi/Desktop/input.jpg")  # change filename
path_out = '/Users/agi/Desktop'

# Magic bytes (true MIME)
mime = magic.from_file(str(path_in), mime=True)
desc = magic.from_file(str(path_in))
print("MIME:", mime)
print("Description:", desc)

# Pillow check
with Image.open(path_in) as im:
    print("Pillow format:", im.format)
    print("Size:", im.size)
    print("Mode:", im.mode)


# unsure of this
pillow_heif.register_heif_opener()
im = Image.open("input.jpg") # actually it's .HEIC
im.save("output_pillow.jxl", quality=90)


## --------- 
## Video Conversion
import subprocess
infile = "input.wmv"
outfile = "output.mp4"

cmd = [
    "ffmpeg", "-i", infile,
    "-map", "0:v:0", "-map", "0:a:0", "-map_metadata", "0",
    "-c:v", "libx265", "-preset", "medium", "-crf", "28",
    "-pix_fmt", "yuv420p", "-tag:v", "hvc1",
    "-c:a", "aac", "-b:a", "160k", "-ac", "2",
    "-movflags", "+faststart",
    outfile
]

subprocess.run(cmd, check=True)