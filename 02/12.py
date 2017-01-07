#!/usr/bin/python
# coding: UTF-8

def write_col(lines, col_num, output_file):
	col = []
	for l in lines:
		col.append(l.split()[col_num] + "\n")
	with open(output_file,"w") as writer:
		writer.writelines(col)
 
f = open('hightemp.txt')
lines = f.readlines()
f.close()

write_col(lines, 0, "col1.txt")
write_col(lines, 1, "col2.txt")