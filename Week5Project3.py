import math
import random

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
guess = random.randint(smaller, larger)
print("You only have", round(math.log(larger - smaller + 1, 2)), "guesses left.")
count = 1

print(guess)
response = input("Am I correct, or is my number too big or small? ")

while response != 'C':
    count += 1
    print(guess)
    response = input("Am I correct, or is my number too big or small? ")
    guess = random.randint(smaller, larger)

if response == 'C':
    print('Good! it took the computer', count, 'try(ies)!')

if response == 'S':
    smaller = guess + 1
    guess = random.randint(smaller, larger)

if response == 'B':
    larger = guess - 1
    guess = random.randint(smaller, larger)
