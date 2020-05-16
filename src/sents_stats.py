# Author: Stratos Mansalis

import math
import pandas
import matplotlib.pyplot as plt
import numpy as np


def sents_len(df, sents):

	"""
		Description 
		------------
		Creating a dataframe with the frequency of the lengths of the sentences
		
		Arguments
		---------
		df: dataframe with the data
		sents : the name of the column with the sentences e.g. 'Sentences'

		Usage
		-----
		e.g df_sents, x, y = sents_len(df, 'Sentence')

		Returns
		-------
		A dataframe with the corresponding lengths of the sentences
		with the frequency for each length

	"""

	df["len"] = " " # create empty columns
	# and filled it with the lens of the sentences
	df["len"] = [len(sent.split()) for sent in df[sents]]

	# create a new df with two columns
	# the first one has the length and the second
	# the frequency sorted by the length
	lengths = df['len'].value_counts().to_frame().reset_index()
	lengths.columns = ['length','total']
	lengths.sort_values(by='length')

	x = lengths['length'].to_list()
	y = lengths['total'].to_list()

	return df, x, y



def len_stats(df):
	'''
	Stats
	'''
	mean_ = df['len'].describe()[1]
	_, mean_l = math.modf(mean_)

	std_ = df['len'].describe()[2]
	_, std_l = math.modf(std_)

	max_ = df['len'].describe()[7]
	_, max_l = math.modf(max_)

	min_ = df['len'].describe()[3]
	_, min_l = math.modf(min_)
	
	return min_l, max_l, mean_l, std_l
