number = int(input("enter number : "))
if number % 2 == 0:
    print("your number is even")
else :
    print("your number is odd")
    


def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

num = int(input("Enter a number: "))

check_even_odd(num)
