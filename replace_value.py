tuple = (1,2,3,4,6,50)
print(tuple)

list = list(tuple)
list[-1] = 6

tuple = tuple(list)
print(tuple)