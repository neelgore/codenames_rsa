import pandas as pd
import numpy as np

vectors = {}
english_words = set()

#with open('wordlist.txt') as wordlist:
#
#	for line in wordlist.readlines():
#		word = line.rstrip('\n')
#		english_words.add(word)

#with open('25d.txt') as glove:
#
#	lines = glove.readlines()
#	print(len(lines))
#
#	for line in lines:
#		line = line.rstrip('\n').split()
#		if line[0] in english_words:
#			vectors[line[0]] = line[1:]
#	
#	print(len(vectors))
#
#with open('25d_trimmed.txt', 'a') as trimmed:
#	
#	for word, vector in vectors.items():
#		trimmed.write(word + ' ')
#		trimmed.write(' '.join(vector))
#		trimmed.write('\n')

#with open('codenames_wordlist.txt', 'r') as codenames_wordlist:
#
#	with open('pog.txt', 'a') as pog:
#
#		lowercased = [word.rstrip('\n').lower() for word in codenames_wordlist.readlines()]
#		pog.write('\n'.join(lowercased))



with open('25d_trimmed.txt') as trimmed:

	with open('25d_trimmed_normalized.txt', 'a') as normalized:

		for line in trimmed.readlines():
			line = line.rstrip('\n').split()
			vectors[line[0]] = [float(num) for num in line[1:]]

		df = pd.DataFrame.from_dict(vectors, orient='index')

		normalized_df = (df - df.mean())/df.std()
		
		for row in normalized_df.iterrows():
			print(row[0], end=' ')
			print(' '.join(str(num) for num in row[1]))
			normalized.write(row[0] + ' ')
			normalized.write(' '.join(str(num) for num in row[1]))
			normalized.write('\n')

	
