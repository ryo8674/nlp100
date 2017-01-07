# coding: UTF-8

raw1 = u"パトカー"
raw2 = u"タクシー"
out = u""

for i in range(len(raw1)):
	out += raw1[i]+raw2[i]
print(out)
