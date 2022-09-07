##5.1-Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints out the the sum of the numbers. Use a for loop.
import random
numDice = int(input("How many dice to roll? "))
sumRoll = 0
for i in range (numDice):
    sumRoll += random.randint(1,6)
print("Sum of all dices is: ", sumRoll)
##5.3--Write a program that asks the user for an integer and tells if the number is a prime number. Prime numbers are number that are only divisible by one or the number itself.
#For example, number 13 is a prime number as can only be divided by 1 or 13 so that the result is an integer.
#On the other hand, number 21 for example is not a prime number as it can be also be divided by numbers 3 and 7.
num = int(input("Input an integer number: "))
halfNum = num // 2
divisible = False
for i in range (2, halfNum+1):
    if num % i == 0:
        divisible = True
        break
if divisible == False:
    print("This is a prime number")
else:
    print("This is not a prime number")