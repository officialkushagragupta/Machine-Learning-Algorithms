def checker(word):
	count = 0
	word = word.lower()
	for i in word:
		if i == 'a' or i == 'e':
			count += 1
	return count