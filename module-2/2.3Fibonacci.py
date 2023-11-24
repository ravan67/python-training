n1 = 0
n2 = 1
num = int(input("enter a fibonacci series: "))

if num == 1:
    print(n1)

else:
    print(n1)
    print(n2)
    for i in range(1,num+1):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3)