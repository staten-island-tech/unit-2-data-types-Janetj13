"""Odd and even numbers"""
""" x = 9
y = 17
if x % 2 == 0 and y % 2==0:
    print("both numbers are even")
elif x % 2==0 or y % 2==0:
    print("at least one number is even")
else:
    print("both numbers are odd") """

"""Tip calculator"""
""" bill = input("How much was your bill? ")
x = float(bill)
tip10 = x * .10
tip15 = x * .15
tip20 = x * .20
tip10 = float(tip10)
tip15 = float(tip15)
tip20 = float(tip20)
total = x + tip10
total = x + tip15
total = x + tip20
tip = input("How much would you like to tip?")
if tip == "10":
    total = x + tip10
    print(f"Your total is ${total:.2f}")
elif tip == "15":
    total = x + tip15
    print(f"Your total is ${total:.2f}")
else:
    total = x + tip20
    print(f"Your total is ${total:.2f}")
 """
"""Factors of a number"""
""" def factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
    if x % i == 0:
        print(i)
number = 15

factors(number)"""

"""Gcf of 2 numbers"""
def gcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            gcf = i 
    return gcf
x = 20
y = 30
print(gcf(x, y))




