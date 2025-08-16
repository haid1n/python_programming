with open("file_io/sample.txt", "r") as file:
	
	for sentence in file:

		print(sentence)

		cap_sentence = sentence.upper()

		print(cap_sentence)