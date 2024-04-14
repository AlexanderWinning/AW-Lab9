def encode(text):
	for i in text:
		if int(i) < 7:
			i += 3
		else:
			i -= 7
	return text
