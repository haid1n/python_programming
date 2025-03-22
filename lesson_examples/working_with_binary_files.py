with open("file_io/photo_2024-07-07_08-56-21.jpg", "rb") as image_file:
	
	image_content = image_file.read()

	print(image_content)