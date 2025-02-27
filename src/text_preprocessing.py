# Author: Stratos Mansalis

import re 
from gensim.parsing.preprocessing import remove_stopwords

def clean_text(x, **kwargs):

	"""
		Description 
		------------
		Cleaning text sentences
		
		Arguments
		---------
		df: dataframe with the data
		stopwords = True (optinal)

		Usage
		-----
		e.g x = clean_text(x)

		Returns
		-------
		A cleaned sentence

	"""

	x = clean_whitespaces(x) 
	x = clean_puncts(x)
	x = clean_whitespaces(x)
	x = x.lower()
	x = replace_contractions(x)
	x = clean_numbers(x)
	for key, value in kwargs.items():
		if key == 'stopwords' and value == 'True':
			x = remove_stopwords(x)

	return x


# Remove Punctuation

def clean_puncts(x):
	x = str(x)
	pattern = r'[^\w\s]'
	x = re.sub(pattern, ' ', x)
	return x

def replace_contractions(x):
	for key in contraction_dict.keys():
		x = x.replace(key, contraction_dict[key])
	return x

# Clean Numbers

def clean_numbers(x):
	if bool(re.search(r'\d', x)): 
		x = re.sub('[0-9]{5,}', ' ', x)
		x = re.sub('[0-9]{4}', '  ', x)
		x = re.sub('[0-9]{3}', ' ', x)
		x = re.sub('[0-9]{2}', ' ', x)
		x = re.sub('[0-9]{1}', ' ', x)
	return x



# Clean Whitespaces

def clean_whitespaces(x):
	x = " ".join(x.split())
	return x



# Contradictions

contraction_dict = {" 's": "is","isn't": "is not", "aren't": "are not","can't": "cannot", "'cause": "because",
"could've": "could have", "couldn't": "could not", "didn't": "did not",  "doesn't": "does not",
"don't": "do not", "hadn't": "had not", "hasn't": "has not", "haven't": "have not", "he'd": "he would",
"he'll": "he will", "he's": "he is", "how'd": "how did", "how'd'y": "how do you", "how'll": "how will",
"how's": "how is",  "I'd": "I would", "I'd've": "I would have", "I'll": "I will", "I'll've": "I will have",
"I'm": "I am", "I've": "I have", "i'd": "i would", "i'd've": "i would have", "i'll": "i will",
"i'll've": "i will have","i'm": "i am", "i've": "i have", "isn't": "is not", "it'd": "it would",
"it'd've": "it would have", "it'll": "it will", "it'll've": "it will have","it's": "it is", "let's": "let us",
"ma'am": "madam", "mayn't": "may not", "might've": "might have","mightn't": "might not",
"mightn't've": "might not have", "must've": "must have", "mustn't": "must not",
"mustn't've": "must not have", "needn't": "need not", "needn't've": "need not have",
"o'clock": "of the clock", "oughtn't": "ought not", "oughtn't've": "ought not have", "shan't": "shall not",
"sha'n't": "shall not", "shan't've": "shall not have", "she'd": "she would", "she'd've": "she would have",
"she'll": "she will", "she'll've": "she will have", "she's": "she is", "should've": "should have",
"shouldn't": "should not", "shouldn't've": "should not have", "so've": "so have","so's": "so as",
"this's": "this is","that'd": "that would", "that'd've": "that would have", "that's": "that is",
"there'd": "there would", "there'd've": "there would have", "there's": "there is", "here's": "here is",
"they'd": "they would", "they'd've": "they would have", "they'll": "they will", "they'll've": "they will have",
"they're": "they are", "they've": "they have", "to've": "to have", "wasn't": "was not", "we'd": "we would",
"we'd've": "we would have", "we'll": "we will", "we'll've": "we will have", "we're": "we are", "we've": "we have",
"weren't": "were not", "what'll": "what will", "what'll've": "what will have", "what're": "what are",
"what's": "what is", "what've": "what have", "when's": "when is", "when've": "when have", "where'd": "where did",
"where's": "where is", "where've": "where have", "who'll": "who will", "who'll've": "who will have",
"who's": "who is", "who've": "who have", "why's": "why is", "why've": "why have",
"will've": "will have", "won't": "will not", "won't've": "will not have",
"would've": "would have", "wouldn't": "would not", "wouldn't've": "would not have",
"y'all": "you all", "y'all'd": "you all would","y'all'd've": "you all would have",
"y'all're": "you all are","y'all've": "you all have","you'd": "you would",
"you'd've": "you would have", "you'll": "you will", "you'll've": "you will have",
"you're": "you are", "you've": "you have"} 
















