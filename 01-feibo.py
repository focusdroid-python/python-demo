num = list()


a = 0
b = 1
i = 0
while i < 20:
	num.append(a)
	a,b = b,a+b
	i+=1

for temp in num:
	print(temp)




"""a = 0
b = 1
i = 0

while i < 20:
	a,b = b, a+b
	print(a)
	i+=1
"""