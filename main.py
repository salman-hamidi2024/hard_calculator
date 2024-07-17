import math
def hard(x):
    number1 = int(x**5//3+math.tan(x))
    number2 = int(math.pi**2+math.tan(math.sin(x)**2)**-1)
    return math.gcd(number1,number2)
user = int(input("enter your number: "))
print(hard(user))