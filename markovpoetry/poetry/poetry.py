import random
import string

import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
english_stopwords = set(stopwords.words('english'))
extra_stopwords = {
	'thy', 'thereof', 
}
english_stopwords.update(extra_stopwords)


def generate_chain():
	chain = {}
	words = []

	with open("corpus/bible.txt") as f:
		for line in f:
			for word in line.split():
			    stripped_word = word.translate(str.maketrans('', '', string.punctuation))
			    stripped_word = stripped_word.lower()
			    words.append(stripped_word)

	# generate markov chain
	for i, word in enumerate(words):
		try: # end of stream
			second_word = words[i+1]
			third_word = words[i+2]
		except:
			continue

		word_pair =  f'{words[i]}_{words[i+1]}'
		if chain.get(word_pair):
			chain[word_pair].append(third_word)
		else:
			chain.update(
				{
					word_pair: [third_word]
				})

	return chain

def generate_sentence(sentence_length=0):
	if sentence_length == 0:
		sentence_length = random.randint(10, 40)
	chain = generate_chain()

	sentence = []
	k = random.choice(list(chain.keys())) # get first word-pair randomly
	sentence.extend(k.split('_'))
	for i in range(sentence_length):
		old_word = k.split('_')[1] 
		new_word = random.choice(chain[k])
		k = f'{old_word}_{new_word}'		

		# don't finish on a stopword
		if i == sentence_length-1:
			while new_word in english_stopwords:
				old_word = k.split('_')[1] 
				new_word = random.choice(chain[k])
				k = f'{old_word}_{new_word}'

		sentence.append(new_word)

	sentence = ' '.join(sentence)
	full_sentence = f'\"{sentence.capitalize()}\"'

	return(full_sentence)

	
generate_sentence()