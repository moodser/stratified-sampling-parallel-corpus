"""
Created on Thu Dec 20 2018

@script: Corpus Splitter Train, Test, Validation

@author: Moodser Hussain
@contact: moodser.hussain@gmail.com	
@org: COMSATS University Islamabad, Lahore Campus, Pakistan

"""

"""

@functionality:
-> This script divide the parallel machine translation corpus into train, test and tune set.
-> Same proportion of each file is used in train, test and tune set.
-> This script support both type of splits (1) Percentage and (2) Number 
-> Place all parallel files of English in 'en' directory and Urdu in 'ur' directory.
-> Place this script in the root directory of 'en' and 'ur' folder.
-> Name of files should end with language extention (e.g. 'en').

"""

####################################
## Acknowledgement
#### Dr. Rao Muhammad Adeel Nawab (Supervisor)
#### Mr. Muhammad Sharjeel (Co-Supervisor)
####################################


# Required Libraries
import random, sys, os, glob, math


# Get the name of files in a list
directory = os.getcwd()
files = sorted(os.listdir(directory+'/en'))
i=0
for thisFile in files:
     files[i] = os.path.splitext(thisFile)[0]
     i=i+1


# Calculation to find total number of sentences (of all files)
# We need this for Number Split
mega_temp=open('mega-temp', 'a+', encoding='utf-8')
for filename in glob.iglob(directory+'/en/*.en'):
	with open(filename, 'r', encoding='utf-8') as textfile:
		mega_temp.writelines(textfile.readlines())
mega_temp.close()
total_corpora_size = sum(1 for line in open('mega-temp', encoding='utf-8'))
mega_temp.close()
os.remove('mega-temp')
print('Total size of corpus is :'+str(total_corpora_size)+' sentences')

# Selection of Corpus Split Type
split_type = input('(1) Percent Split or (2) Number Split?: ')
if (split_type==1):
	test_percent=input('Percentage of Test Sentences?: ')
	tune_percent=input('Percentage of Tune Sentences?: ')
else:
	test_sent=input('Number of Test Sentences?: ')
	tune_sent=input('Number of Tune Sentences?: ')

	test_quota=(float(test_sent)/total_corpora_size)
	tune_quota=(float(tune_sent)/total_corpora_size)
	

# Output Files of English Sentences
output_en_train = open('train.en', 'a+', encoding='utf-8')
output_en_tune = open('tune.en', 'a+', encoding='utf-8')
output_en_test = open('test.en', 'a+', encoding='utf-8')

# Output Files of Urdu Sentences
output_ur_train = open('train.ur', 'a+', encoding='utf-8')
output_ur_tune = open('tune.ur', 'a+', encoding='utf-8')
output_ur_test = open('test.ur', 'a+', encoding='utf-8')

for filename in files:
	lines_en = open('en/'+filename+'.en', 'r', encoding='utf-8').readlines()
	lines_ur = open('ur/'+filename+'.ur', 'r', encoding='utf-8').readlines()
	
	# Combining Both Files - To keep parallel sentences intact
	combined_data = list(zip(lines_en, lines_ur))
	random.shuffle(combined_data)
	lines_en, lines_ur = zip(*combined_data)

	# Writing Randomized Data to Temporary Corpus Files
	open('temp_corp.en', 'w', encoding='utf-8').writelines(lines_en)
	open('temp_corp.ur', 'w', encoding='utf-8').writelines(lines_ur)

	# Reading Randomized Data
	lines_en = open('temp_corp.en', encoding='utf-8').readlines()
	lines_ur = open('temp_corp.ur', encoding='utf-8').readlines()

	# Some Calculations 
	# According to Selected Split Settings
	############################
	############################
	if (split_type==1):
		total_data = int(len(lines_en))
		testing_data = int(math.ceil((total_data*test_percent)/100))
		tuning_data = int(math.ceil((total_data*tune_percent)/100))
	else:
		total_data = len(lines_en)
		testing_data = int(math.ceil(total_data*test_quota))
		tuning_data = int(math.ceil(total_data*tune_quota))

	# Splitting Parallel Sentences
	test_lines_en = lines_en[0:testing_data]
	test_lines_ur = lines_ur[0:testing_data]
	tune_lines_en = lines_en[testing_data:(testing_data+tuning_data)]
	tune_lines_ur = lines_ur[testing_data:(testing_data+tuning_data)]
	train_lines_en = lines_en[testing_data+tuning_data:total_data]
	train_lines_ur = lines_ur[testing_data+tuning_data:total_data]

	# Writing Data back in Seperate Files
	output_en_train.writelines(train_lines_en)
	output_ur_train.writelines(train_lines_ur)
	
	output_en_test.writelines(test_lines_en)
	output_ur_test.writelines(test_lines_ur)
	
	output_en_tune.writelines(tune_lines_en)
	output_ur_tune.writelines(tune_lines_ur)

	# Removing Temporary Files
	os.remove('temp_corp.en')
	os.remove('temp_corp.ur')
