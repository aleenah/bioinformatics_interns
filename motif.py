#!/usr/bin/env python3

#gaining access to regular expression module
import re

#set variable equal to kmer 
sixmer = "TGGCGA"

#open file with sequence to read it , set handle
with open ("og_seq.fasta", "r") as in_handle:
	sequence = in_handle.read()
	
#interpret handle and set interpretation to variable
seq = str(sequence)

#turn variable holding read file into a collection of strings
seq_list = sequence.split(sixmer)

#print list of split strings
print(seq_list)

#take first item in list of split strings, out of the list
seq_list.remove(seq_list[0])

#print list of split strings (sans first item)
print(seq_list)

#create function that takes in two parameters
def prepend(list, str):

#store an item from the list in a string that as changing each iteration
	str += "{0}"
	
#break string at desired kmer, creating a list and save as variable
	list = [str.format(i) for i in list]
	
#call function with parameters list of split strings and kmer variable
#retreive list from function
	return (list)

#assign output from function to variable 
repeat_list = prepend(seq_list, sixmer)

#iterate through function output
for item in repeat_list:
	
#print iteration of function output
	print(item)

	
	
#create a dictionary that contains split strings and kmer variable
#take last item in list of split strings, out of list
#sort list of split strings without the first item
#the two parameters take in two different collections
