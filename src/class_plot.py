# Author: Stratos Mansalis

import math
import pandas
import matplotlib.pyplot as plt
import numpy as np

from class_ratio import ratio_


def plot_v(train, test, tag, **kwargs):

	"""
		Description (Vertical bars Plot)
		------------
		Plot the distribution of the classes in both
		traning and test set in one figure.
		

		Arguments
		---------
		train: train dataset
		test : test dataset
		tag: the name of the class column
		hor (optinal)
		ver (optinal) 
		hor_dist (optinal)
		per_dist (optinal)

		Usage
		-----
		e.g plot_v(train, test, 'class', hor = 18, ver = 10)

		Returns
		-------
		One figure with two axes, one for the train set
		and one for the test set.

		"""

###############################################
# Figure Size (Optional)
# hor: horizontal, ver: vertical
###############################################

	hor, ver = 14, 6

	for key, value in kwargs.items():
		#print ("%s == %s" %(key, value))
		#print(key)
		if key == 'hor':
			hor = value
		elif key == 'ver': 
			ver = value

###############################################
# Annotation above bars distance
# per_dist: percent of the bars distance
# hor_dist: horizontal distance
###############################################

	per_dist, ver_dist = 1.15, 1000

	for key, value in kwargs.items():  

		if key == 'per_dist':
			per_dist = value
		elif key == 'ver_dist':
			ver_dist = value

###############################################

	df_train = ratio_(train, tag)
	df_test = ratio_(test, tag)
	
	total1 = df_train['Total'].sum()
	max1 = df_train['Total'].max()
	total2 = df_test['Total'].sum()
	max2 = df_test['Total'].max()
	total_sum = total1 + total2


	
	###############################################
	# Create Figure and the corresponding title   #
	###############################################

	fig = plt.figure(figsize=(hor, ver))
	
	fig.text(x=0.55, y=0.98, s="Number of Samples per Class", fontsize=15, fontweight='bold', ha="center", transform=fig.transFigure)
	fig.text(x=0.55, y=0.94, s= "How many samples each class has?", fontsize=13, ha="center", transform=fig.transFigure)

	#############################
	#         AXES 1            #
	#############################

	ax1 = fig.add_subplot(1, 2 ,1)
	ax1.set_title('Training Set', size=14, fontweight='bold',color='royalblue')

	# Custom X - label
	ax1.set_xlabel('Class', size=14, fontweight='bold')
	# Custom Y - label
	ax1.set_ylabel('Number of Training Instances', size=14, fontweight='bold')

	# Custom X axis-ticks
	ax1.set_xticklabels(df_train['Class'], size = 10) 
	ax1.set_xticks(df_train['Class'])

	# Custom Y axis-ticks
	t_max = df_train['Total'].max()
	step = t_max/8
	_, step = math.modf(step)
	step = int(step)
	
	max1 = df_train['Total'].max()+(2*step)
	y_ticks = np.arange(0, max1+step, step)
	
	yrange = (y_ticks[0], y_ticks[-1])
	ax1.set_ylim(yrange)
	ax1.set_yticklabels(y_ticks, size = 12)
	ax1.set_yticks(y_ticks)
	 
	# Create bar
	ax1.bar(df_train['Class'], df_train['Total'], color='dodgerblue', edgecolor='black')

	# Annotate
	rects = ax1.patches
	

	for i,rect in enumerate(rects): # for each bar 
		percentage = rect.get_height()/total1 # estimate the percentage
		percentage = '{:.1f}%'.format(100 * percentage)  
		height = rect.get_height()
		ax1.text(rect.get_x() + rect.get_width() / 2, (per_dist*rect.get_height())+ver_dist, '%s\n(%s)'% (height, percentage),
				 ha='center', va='bottom', color = 'black', size = 12)
		
	#############################
	#          AXES 2           #
	#############################
	

	ax2 = fig.add_subplot(1, 2 ,2)
	ax2.set_title('Test Set', size=14, fontweight='bold',color='royalblue')
	
	# Custom X - label
	ax2.set_xlabel('Class', size=14, fontweight='bold')

	# Custom X axis-ticks
	ax2.set_xticklabels(df_test['Class'], size = 10) 
	ax2.set_xticks(df_test['Class'])

	# Custom Y axis-ticks
	t_max = df_train['Total'].max()
	step = t_max/8
	_, step = math.modf(step)
	step = int(step)
	max1 = df_train['Total'].max()+(2*step)
	y_ticks2 = np.arange(0, max1+step, step)
	yrange = (y_ticks2[0], y_ticks2[-1])
	ax2.set_ylim(yrange)
	ax2.set_yticklabels(y_ticks2, size = 12)
	ax2.set_yticks(y_ticks2)
	 
	# Create bar
	ax2.bar(df_test['Class'], df_test['Total'], color='dodgerblue', edgecolor='black')

	# Annotation
	rects2 = ax2.patches

	for i,rect2 in enumerate(rects2): # for each bar 
		percentage2 = rect2.get_height()/total2 # estimate the percentage
		percentage2 = '{:.1f}%'.format(100 * percentage2)  
		height2 = rect2.get_height()
		ax2.text(rect2.get_x() + rect2.get_width() / 2, (per_dist*rect2.get_height()) + ver_dist, '%s\n(%s)'% (height2, percentage2),
				 ha='center', va='bottom', color = 'black', size = 11)  
	sum_total = total1+total2 
	
	
	# Annotate
	ax2.annotate('Train: {:.1f}%\n Test: {:.1f}%'.format((100*total1/sum_total), 100*total2/sum_total), xy=(1, 1), xycoords='axes fraction', fontsize=13,
				xytext=(-15, -15), textcoords='offset points',
				ha='right', va='top',bbox={'facecolor': 'yellow', 'alpha': 0.20, 'pad': 5})

	# Figure Layout
	fig.tight_layout(rect=[0, 0.03, 1, 0.95])








def plot_h(train, test, tag, **kwargs):

	"""
		Description (Horizonal bars Plot)
		------------
		Plot the distribution of the classes in both
		traning and test set in one figure.
		

		Arguments
		---------
		train: train dataset
		test : test dataset
		tag: the name of the class column
		hor (optinal)
		ver (optinal) 
		hor_dist (optinal)
		per_dist (optinal)

		Usage
		-----
		e.g plot_h(train, test, 'class', hor = 18, ver = 10)

		Returns
		-------
		One figure with two axes, one for the train set
		and one for the test set.

		"""


###############################################
# Figure Size (Optional)
# hor: horizontal, ver: vertical
###############################################

	hor, ver = 14, 10

	for key, value in kwargs.items():
		#print ("%s == %s" %(key, value))
		#print(key)
		if key == 'hor':
			hor = value
		elif key == 'ver':
			ver = value

###############################################


###############################################
# Annotation above bars distance
# per_dist: percent of the bars distance
# hor_dist: horizontal distance
###############################################

	per_dist, hor_dist = 1.15, 5000

	for key, value in kwargs.items():  
		#print ("%s == %s" %(key, value))
		#print(key)
		if key == 'per_dist':
			per_dist = value
		elif key == 'hor_dist':
			hor_dist = value

###############################################


	df_train = ratio_(train, tag)
	df_test = ratio_(test, tag)

	
	total1 = df_train['Total'].sum()
	max1 = df_train['Total'].max()
	total2 = df_test['Total'].sum()
	max2 = df_test['Total'].max()
	total_sum = total1 + total2
	
	###############################################
	# Create Figure and the corresponding title   #
	###############################################
	
	fig = plt.figure(figsize=(hor, ver))
	fig.suptitle('Number of Instances', fontsize=17, fontweight='bold') 

	###############################
	# AXES 1                      #
	###############################
	
	# Title
	ax1 = fig.add_subplot(1, 2, 1)
	ax1.set_title('Train Set', size=14, fontweight='bold', color='dodgerblue')

	# Custom X - label
	ax1.set_xlabel('Number of Instances', size=14, fontweight='bold')

	# Custom Y - label
	ax1.set_ylabel('Class', size=15, fontweight='bold')

	# Custom Y axis-ticks
	ax1.set_yticklabels(df_train['Class'], size = 12) 

	# Custom X axis-ticks
	stepx = max1/6
	_, stepx = math.modf(stepx)
	stepx = int(stepx)	
	x_ticks = np.arange(0, max1+(2*stepx), stepx)
	xrange = (x_ticks[0], x_ticks[-1])
	ax1.set_xlim(xrange)
	ax1.set_xticklabels(x_ticks, size = 12)
	ax1.set_xticks(x_ticks)

	# Grid
	ax1.grid(which='major', axis='x',color='black', linestyle='--', linewidth=0.5, alpha=0.5 )
	ax1.grid(which='minor', axis='x',color='black', linestyle='--',  alpha=0.2)
	ax1.set_axisbelow(True)

	# Create bar
	ax1.barh(df_train['Class'], df_train['Total'], edgecolor='black')
	ax1.invert_yaxis()

	rects = ax1.patches

	for i, rect in enumerate(rects): # for each bar
		width = rect.get_width()
		ax1.text(per_dist*rect.get_width()+hor_dist, rect.get_y()+(0.5*rect.get_height()),
				 '%d' % int(width), ha='center', va='center', size = 13)
	
	###############################
	# AXES 2                      #
	###############################
	
	ax2 = fig.add_subplot(1, 2, 2)
	ax2.set_title('Test Set', size=14, fontweight='bold', color='dodgerblue')

	# Custom X - label
	ax2.set_xlabel('Number of Instances', size=14, fontweight='bold')

	# Custom Y - label
	#ax2.set_ylabel('Class', size=16, fontweight='bold')
 
	# Custom Y axis-ticks
	ax2.set_yticklabels(df_test['Class'], size = 12) 

	# Custom X axis-ticks
	stepx2 = max1/6
	_, stepx2 = math.modf(stepx2)
	stepx2 = int(stepx2)	
	x_ticks2 = np.arange(0, max1+(2*stepx2), stepx2)
	xrange2 = (x_ticks2[0], x_ticks2[-1])
	ax2.set_xlim(xrange2)
	ax2.set_xticklabels(x_ticks2, size = 12)
	ax2.set_xticks(x_ticks2)
	

	# Grid
	ax2.grid(which='major', axis='x',color='black', linestyle='--', linewidth=0.5, alpha=0.5 )
	ax2.grid(which='minor', axis='x',color='black', linestyle='--',  alpha=0.2)
	ax2.set_axisbelow(True)

	# Create bar
	ax2.barh(df_test['Class'], df_test['Total'], edgecolor='black')
	ax2.invert_yaxis()
	
	# Annotate
	rects2 = ax2.patches
	for i, rect2 in enumerate(rects2): # for each bar
		width = rect2.get_width()
		ax2.text(per_dist*rect2.get_width()+hor_dist, rect2.get_y()+(0.5*rect2.get_height()),
				 '%d' % int(width), ha='center', va='center', size = 13)
	
	train_percent = total1/total_sum
	test_percent = total2/total_sum
	
	ax2.annotate("Total: {}\nTrain: {} ({:.0f}%)\nTest: {} ({:.0f}%)".format(total_sum, total1,100*train_percent, total2, 100*test_percent) , xy=(1, 0), xycoords='axes fraction', fontsize=13,
				 xytext=(-15, 75), textcoords='offset points', ha='right', va='top',bbox={'facecolor': 'yellow', 'alpha': 0.25, 'pad': 5})

	
	fig.tight_layout(rect=[0, 0.03, 1, 0.95])
