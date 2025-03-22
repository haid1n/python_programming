with open("file_io/photo_2024-07-07_08-56-21.jpg", "rb") as image_file, open("file_io/image_copy.jpg", "wb") as duplicate_image:
	duplicate_image.write(image_file.read())