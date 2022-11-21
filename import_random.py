import random
def random_line(fname):
    f=open(fname).read().splitlines()
    print(random.choice(f))

random_line("nik67.text")