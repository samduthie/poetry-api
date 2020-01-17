#read in text.
'''
every 2 words = key
	add w3 to the list of values for that key

printing:
	print w1, w2
	find random w3
	print w2 w3

'''
import string

words = []

with open("corpus/bible.txt") as f:
	for line in f:
		for word in line.split():
		    stripped_word = word.translate(str.maketrans('', '', string.punctuation))
		    stripped_word = stripped_word.lower()
		    words.append(stripped_word)


chain = {}

# generate markov chain
for i, word in enumerate(words):
	try: # end of stream
		second_word = words[i+1]
		third_word = words[i+2]
	except:
		continue

	word_pair =  f'{words[i]}_{words[i+1]}'
	# print(word_pair)
	if chain.get(word_pair):
		chain[word_pair].append(third_word)
	else:
		chain.update(
			{
				word_pair: [third_word]
			})

import random

poem_length = 40

sentence = []
k = random.choice(list(chain.keys())) # get first word-pair randomly
sentence.extend(k.split('_'))
for i in range(poem_length):
	old_word = k.split('_')[1] 
	new_word = random.choice(chain[k])
	sentence.append(new_word)
	k = f'{old_word}_{new_word}'

print(' '.join(sentence))

	
