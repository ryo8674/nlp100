# -*- coding: utf-8 -*-

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine.\
 New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words_list = str.split()

dict = {}
single = [0, 4, 5, 6, 7, 8, 14, 15, 18]

for i in range(len(words_list)):
    clen = 1 if i in single else 2
    dict[words_list[i][:clen]] = i + 1

# 原子番号順にソートして print（蛇足）
for k, v in sorted(dict.items(), key=lambda x:x[1]):
    print (k, v)