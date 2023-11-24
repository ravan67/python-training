l1 = ['ab', 'abc' , 'abcd', '124']

def compare(l1):
    a = 0 
    for i in l1:
        if len(i)>1 and i(0) == i[-1]:
            a += 1
    
    return a


