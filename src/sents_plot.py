# Author: Stratos Mansalis

import math
import pandas
import matplotlib.pyplot as plt
import numpy as np


from sents_stats import sents_len
from sents_stats import len_stats

def len_plot(df, sents, **kwargs):


	"""
		Description 
		------------
		Plot the distribution of the length of the sentences
		Note! You need the sents_stat module in order to run it!
		
		Arguments
		---------
		df: dataframe with the data
		sents : the name of the column with the sentences e.g. 'Sentences'
		hor: figure horizontal size (optinal)
		ver: figure vertical size (optinal) 

		Usage
		-----
		e.g len_plot(df, 'Sentence', hor = 18, ver = 10)

		Returns
		-------
		One Figure with the distribution of the length of the sentences

	"""


	###############################################
	# Figure Size (Optional)
	#
	# hor: horizontal, ver: vertical
	###############################################

	hor, ver = 20, 12

	for key, value in kwargs.items():
		#print ("%s == %s" %(key, value))
		#print(key)
		if key == 'hor':
			hor = value
		else:
			ver = value

	###############################################
	
	df,x1,y1 = sents_len(df, sents)
	min_l, max_l, mean_l, std_l = len_stats(df)
	
	# Create Figure
	fig = plt.figure(figsize=(hor, ver))

	# Create axes
	ax = fig.add_subplot(2, 2, 1)
	ax.set_title('Length of Sentences', size=16, fontweight='bold')

	# Custom X - label
	ax.set_xlabel('Length', size=14, fontweight='bold')

	# Custom Y - label
	ax.set_ylabel('Number of Sentences', size=14, fontweight='bold')

	# Custom X axis-ticks
	step = max(x1)/8
	_, step = math.modf(step)
	step = int(step)
	x_ticks = np.arange(0, max(x1)+2,step)
	xrange = (x_ticks[0], x_ticks[-1])
	ax.set_xlim(xrange)
	ax.set_xticklabels(x_ticks, size = 14)  
	ax.set_xticks(x_ticks)

	# Custom Y axis-ticks
	stepy = max(y1)/12
	_, stepy = math.modf(stepy)
	stepy = int(stepy)
	y_ticks = np.arange(0, max(y1)+(2*stepy), stepy)
	yrange = (y_ticks[0], y_ticks[-1])
	ax.set_ylim(yrange)
	ax.set_yticklabels(y_ticks, size = 14)
	ax.set_yticks(y_ticks)    

	# Create bar
	ax.bar(x1, y1, color='dodgerblue')
	
	min_len, max_len, mean_len, std_len = len_stats(df)
	
	# Annotate
	ax.annotate('Mean: %s\nMin: %s\nMax: %s\nStd: %s '% (mean_len,min_len, max_len, std_len), xy=(1, 1), xycoords='axes fraction', fontsize=13,
				xytext=(-15, -15), textcoords='offset points',
				ha='right', va='top',bbox={'facecolor': 'yellow', 'alpha': 0.20, 'pad': 5})
	ax.grid(which='major', axis='y',color='black', linestyle='--', linewidth=0.3 )

	fig.tight_layout(rect=[0, 0.03, 1, 0.95])
