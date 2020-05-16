# author: Stratos Mansalis 

import pandas as pd
from nltk.tokenize import word_tokenize
from collections import Counter


def vocabulary_builder(df, sents):


    """
        Description 
        ------------
        Creates the vocabulary and the corresponding index for the given dataset.
        

        Arguments
        ---------
        df: the name of the dataframe
        sents: the name of the column of the corresponding 
        

        Usage
        -----
        e.g most_common_words(train, 'Sentence', 'class', 0, top=15)

        Returns
        -------
        the vocabulary (words)
        Dictionaries to store the word to index mappings (word2idx) and vice versa (idx2word)

    """

	words = Counter()

	# tokenize the sentences, add them to a new column
	df["sentences_tokenize"] = df[sents].apply(lambda x: word_tokenize(x)) 

	# a list of lists with the tokenized sentences
	train_sentences = df[sents].to_list() 

	# for each sentence
	for i, sentence in enumerate(train_sentences): 
		train_sentences[i] = [] 
		for word in word_tokenize(sentence):
			words.update([word]) 
			train_sentences[i].append(word)

	# Removing the words that only appear once
	words = {k:v for k,v in words.items() if v>1}

	# Sorting the words according to the number of appearances, with the most common word being first
	words = sorted(words, key=words.get, reverse=True)

	# Adding padding and unknown to our vocabulary so that they will be assigned an index
	words = ['_PAD','_UNK'] + words

	# Dictionaries to store the word to index mappings and vice versa
	word2idx = {o:i for i,o in enumerate(words)}
	idx2word = {i:o for i,o in enumerate(words)}

	return words, word2idx, idx2word
