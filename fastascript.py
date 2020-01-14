#!/usr/bin/env python3
import argparse
import random
import os
#importing libraries

#parser = argparse.ArgumentParser(description = "please give a header")
#parser.add_argument(-"h", "-header") 
#args = parser.parse_args()

nuc_list= ["A","T","C","G"]
 
def repeat_seq(length):
    your_letters='ATCG'
    return ''.join((random.choice(your_letters) for i in range(length)))
#this function creates a random string of actgs with a specific length.
 
#new_fasta is the name of our fasta function

repeat_seq1= repeat_seq(30)
repeat_seq2= repeat_seq(30)
repeat_seq3= repeat_seq(30)
repeat_seq4= repeat_seq(30)
repeat_seq5= repeat_seq(30)
#this creates 5 random requences with the same length (30)

def new_fasta():
 
	try:
		with open("psuedo_protein.fasta","w") as in_handle:
			#in_handle.write(args.header)
			#in_handle.write("\r")
			in_handle.write(repeat_seq1)
			in_handle.write(repeat_seq2)
			in_handle.write(repeat_seq3)
			in_handle.write(repeat_seq4)
			in_handle.write(repeat_seq5)
			in_handle.write(repeat_seq1)
			in_handle.write(repeat_seq2)
			in_handle.write(repeat_seq3)
			in_handle.write(repeat_seq4)
			in_handle.write(repeat_seq5)
		return(in_handle)
#opens file and writes sequences to it   

	except IOError as err:
#this is the exception error that will help skip over syntax errors
			print("IOError")

print(new_fasta())
#calling new fasta function
