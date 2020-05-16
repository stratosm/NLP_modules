# Author: Stratos Mansalis

import pandas as pd
import numpy as np



def pad_input(sentences, seq_len):

	"""
        Description 
        ------------
        Defining a function that either shortens sentences or pads sentences with 0 to a fixed length
        

        Arguments
        ---------
        sentences: the corresponding sentences
        seq_len: the max len of the sentences
        

        Usage
        -----
        e.g train_sentences_ = pad_input(train_sentences, seq_len)



        Returns
        -------
        the padding sentence

    """

    features = np.zeros((len(sentences), seq_len), dtype=int)
    for ii, review in enumerate(sentences):
        if len(review) != 0:
            features[ii, -len(review):] = np.array(review)[:seq_len]

    return features
