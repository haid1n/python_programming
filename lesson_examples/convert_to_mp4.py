## Imported modules ##
from moviepy import VideoFileClip

import os

## Function for converting file to mp4 ##
def convert_to_mp4(input_file, output_file):
	video = VideoFileClip(input_file)

	video.write_videofile(output_file, codec="libx264")

directory = r"C:\Users\chari plus\OneDrive\Videos\SnapTube"

file = "GOJO SONG _ _Who's Next__ _ Divide Music [Jujutsu Kaisen].webm"

source_file = os.path.join(directory, file)

input_file = source_file

output_file = "GOJO SONG.mp4"

convert_to_mp4(input_file, output_file)
