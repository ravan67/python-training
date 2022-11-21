tuple = ('i', 'a','m', 'n','i','k','h','i','l')
print(type(tuple))


def convert(tuple):


    string =""
    for i in tuple:
        string = string+i
    return string
string = convert(tuple)
print(string)
print(type(string))
