# author: Stratos Mansalis

import pandas as pd 
import numpy as np 
from nltk.tokenize import word_tokenize 


def word2idx_(df, sents, wordsindex):

	    """
        Description 
        ------------
        convert the words in the sentences to their corresponding indexes.
        

        Arguments
        ---------
        df: the name of the dataframe
        sents: the name of the column of the corresponding 
        wordsindex: the index of the words
        

        Usage
        -----
        e.g train_sentences = word2idx_(train, 'Sentence', word2idx)


        Returns
        -------
        the sentences with their corresponding indexes

    """

    sentences = df[sents].to_list()

    for i, sentence in enumerate(sentences):
        sentences[i] = [wordsindex[word] if word in wordsindex else 0 for word in word_tokenize(sentence)]

    return sentences
