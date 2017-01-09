zoo = ('panda', 'crocodile', 'zebra', 'lion', 'tiger', 'monkey')
print(zoo)
print(zoo[0])

for x in zoo:
	print(x)

(cage1, cage2, cage3, cage4, cage5, cage6) = zoo
print(cage1)
print(cage3)

list_zoo = list(zoo)
print(list_zoo)

list_zoo.extend(['dragon', 'wolf', 'flamingo'])
print(list_zoo)

back_to_tuple = tuple(list_zoo)
print(back_to_tuple)