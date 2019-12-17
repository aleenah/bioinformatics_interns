!/usr/bin/env python3
import argparse
import FileIO
import random
import Random
import OS
import numpy as np
#importing libraries

parser = argparse.ArgumentParser(description = "please give a header")
parser.add_argument("header", required) 
args = parser.parse_args()

nuc_list= ["A","T","C","G"]
 
def repeat_seq(length):
    your_letters='ATCG'
    return ''.join((random.choice(your_letters) for i in range(length)))
#this function creates a random string of actgs with a specific lenght.
 
new_fasta is the name of our fasta function
repeat_seq1= repeat_seq(30)
repeat_seq2= repeat_seq(30)
repeat_seq3= repeat_seq(30)
repeat_seq4= repeat_seq(30)
repeat_seq5= repeat_seq(30)
#this creates 5 random requences with the same length (30)

def new_fasta():
 
	try:
		with open("psuedo_protein.fasta",w) as in_handle:
			in_handle.write(repeat_seq1, repeat_seq2, repeat_seq3, repeat_seq4, repeat_seq5)
#opens file and writes sequences to it   

	except as IOError:
#this is the exception error that will help skip over syntax errors
			print("IOError")
