# Exercise 1.1 Calculating the volume

radius = float(input('Type the radius to calculate the volume'))
def get_sphere_volume(radius):
    pi = 3.14
    volume = (4/3) * pi * radius * radius * radius
    return volume
print("The volume of the sphere is", get_sphere_volume(radius))

# Exercise 1.2a Calculating factorial using recursion

n = float(input('Give a number to calculate a factorial'))
def recursive_factorial(n):
    if n == 1:
        return n
    else:
        return n * recursive_factorial(n-1)
if n < 0:
    print("Cannot be calculating for negative number")
elif n == 0:
    print("Factorial of 0 is 1")
else:
     print("Factorial of", n, "is", recursive_factorial(n))

# Exercise 1.2b Calculating factorial without recursion
import math
n = int(input('Give a number one more time :)'))
math.factorial(n)
print("Factorial of", n, "is", math.factorial(n))

# Exercise 1.3a Printing odd numbers using recursivity

n = int(input('okay, lets do it again, give a number'))
def  recursive_count_up(n, odd):
    if n >= 0:
        recursive_count_up(n-1, odd)
        if odd is False:
            print(n)
        else:
            if (n % 2 != 0):
                print(n)
recursive_count_up(n, False)
#recursive_count_up(n, True) ## If we want to get only odd numbers

# Exercise 1.3b Printing odd numbers without recursivity
n = int(input('give a number (the last time)'))
def count_up(n, odd):
    if odd == True:
        for number in range(0,n+1):
            if (number % 2 != 0):
                print(number)
    else:
        for number in range(0,n+1):
            print(number)
recursive_count_up(n, True)
#recursive_count_up(n, False) ## If we want to get all numbers


# Exercise 1.4

price = float(input('Write a price'))
discount_percentage = 10
def get_final_price(discount_percentage, price):
    discount = price / 100 * 10
    final_price = price - discount
    return final_price
print("price after discount is", get_final_price(discount_percentage, price))
