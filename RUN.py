# parse_vote.py
# extract_qid.py
# training_set.py
# load.py


#from pandas import Series, DataFrame
from parse_vote import *
from extract_qid import *
from training_set import *
from load import *
'''
import pandas as pd
import numpy as np
import json
import string
'''

FILE = 'Arthritis'

PATH_IN  = './' + FILE + '/'
PATH_OUT = './' + FILE + '/'

#generate_qapair(PATH_IN, PATH_OUT);

#extract_qid(PATH_IN, PATH_OUT);

#filter_qid(PATH_IN, PATH_OUT);

#format_data(PATH_IN, PATH_OUT, FILE)

filenames = [   './Allergy/Allergy.csv',
                './Depression/Depression.csv',
                './Arthritis/Arthritis.csv',
                './Alzheimer/Alzheimer.csv' ]

with open('./Total.csv','w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())









