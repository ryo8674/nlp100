#!/usr/bin/python
# coding: UTF-8
import sys

f = open('hightemp.txt')
lines = f.readlines()
f.close()

for l in lines[len(lines) - int(sys.argv[1]):]:
    print l,