#!/usr/bin/python
# coding: UTF-8
 
f = open('hightemp.txt')
lines = f.readlines()
f.close()

for l in lines:
	if "\t" in l:
		l = l.replace("\t"," ")
	print l