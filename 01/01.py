# -*- coding: utf-8 -*-

raw = u"パタトクカシーー"
out = ""
for i, str in enumerate(raw):
	if i % 2 == 0:
		out += str
print(out)
