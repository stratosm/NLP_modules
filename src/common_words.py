import pandas as pd
from collections import Counter

def most_common_words(df, sentence, cl, label, **kwargs):

    """
        Description (Vertical bars Plot)
        ------------
        Print the most common words between the sentnces for the given class
        in a dataframe
        

        Arguments
        ---------
        df: train dataset
        sentence: test dataset
        cl: the name of the class column
        label:
        

        Usage
        -----
        e.g most_common_words(train, 'Sentence', 'class', 0, top=15)

        Returns
        -------
        the most common words

    """

    df_ = df[df[cl]==label]
    df_ = df_[sentence].tolist()
    docx = ' '.join(str(x) for x in df_)
    docx = docx.split()
    word_counter = Counter(docx)

    top = 10

    for key, value in kwargs.items():
        if key == 'top':
            top = value

    for word, count in word_counter.most_common(top):
        print(word, ': ', count)   
