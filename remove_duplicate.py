# remove to duplicate value form list

l1 = [1,2,1,42,12,42,4,5,4]
l2 = set(l1)
l1 = list(l2)
print(l1)