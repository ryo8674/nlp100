#!/usr/bin/python
# coding: UTF-8
 
f = open('hightemp.txt')
lines = f.readlines()
f.close()

count = 0
for l in lines:
	count += 1

print count