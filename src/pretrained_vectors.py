# Author: Stratos Mansalis

import numpy as np

def creating_matrix(glove_dir, embed_size, words ):
	print('------------------------------------------------------------')
	print('Loading',glove_dir,'file ...')
	
	embeddings_index = {}
	f = open(glove_dir)
	for line in f:
		try:
			values = line.split() # for each word break 
			word = values[0] # extract the word from the word embedding
			vector = np.asarray(values[1:], dtype='float32') # extract the embedding
			embeddings_index[word] = vector # save the word as key in the index with the values as the vector
		except:
			#print(word)
			passembed_size=embed_size
	f.close()
	print('A total of %s word vectors loaded.' % len(embeddings_index))
	
	words_covered = 0
	for word in words:
		if word in embeddings_index:
			words_covered += 1
	words_covered_percent = words_covered/len(words)
	print('Pre-trained word embeddings cover {:.2%} of vocabulary'.format(words_covered_percent))
	print('Creating embedding matrix ...')
	embedding_matrix = np.zeros((len(words) + 1, embed_size))
	embedding_matrix.shape
	
	absent_words = 0
	for i,word in enumerate(words):
		embedding_vector = embeddings_index.get(word)
		if embedding_vector is not None:
			# words not found in embedding index will be all-zeros.
			embedding_matrix[i] = embedding_vector
		else:
			#print(word)
			absent_words += 1
	print('Total absent words are', absent_words, 'which is', "%0.2f" % (absent_words * 100 / len(words)), '% of total words')
	print('Embeding matrix created of shape:',embedding_matrix.shape)
	print('-------------------------------------------------------------')
	
	return embedding_matrix 
