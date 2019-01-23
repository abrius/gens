import itertools
res = itertools.product('0123456789', repeat=20)
for i in res:
	numbers=''.join(i)
	print (numbers)
