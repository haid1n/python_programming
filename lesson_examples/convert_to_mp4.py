## Imported modules ##
from moviepy import VideoFileClip


## Function for converting file to mp4 ##
def convert_to_mp4(input_file, output_file):
	video = VideoFileClip(input_file)

	video.write_videofile(output_file, codec="libx264")



input_file = "beserk_ep1"

output_file = "given.mp4"

convert_to_mp4(input_file, output_file)
