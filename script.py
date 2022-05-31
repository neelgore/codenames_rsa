
vectors = {}
english_words = set()

with open('wordlist.txt') as wordlist:
	for line in wordlist.readlines():
		word = line.rstrip('\n')
		english_words.add(word)

with open('25d.txt') as glove:

	lines = glove.readlines()
	print(len(lines))

	for line in lines:
		line = line.rstrip('\n').split()
		if line[0] in english_words:
			vectors[line[0]] = line[1:]
	
	print(len(vectors))

with open('25d_trimmed.txt', 'a') as trimmed:
	
	for word, vector in vectors.items():
		trimmed.write(word + ' ')
		trimmed.write(' '.join(vector))
		trimmed.write('\n')


	
