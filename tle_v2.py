#!/usr/bin/env python

import os
import sys
import glob   
import csv
import fileinput
import lxml
import itertools
from os import listdir
from collections import Counter
sys.path.append('/home/yassine/twtads/KafNafParserPy')
from KafNafParserMod import *



for files in os.listdir('input/'):

	processed_biography = KafNafParser('input/'+files)    
	target = open('termlayer.csv','w')

	for term_obj in processed_biography.get_terms():
		target_text = (term_obj.get_pos(), term_obj.get_lemma()) 
		target.write(target_text.encode('utf-8'))	

	target.close()