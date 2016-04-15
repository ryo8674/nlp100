# -*- coding: utf-8 -*-

original = "I am an NLPer"

def ngram(input, n):
    last = len(input) - n + 1
    ret = []
    for i in range(0, last):
        ret.append(input[i:i+n])
    print (ret)

ngram(original, 2)              # 文字 n-gram
original = original.split()
ngram(original, 2)              # 単語 n-gram