#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
#number = randint(1, 20)
# For Testing: print(aRandomNumber)
number = 10
times = 3
guess = int(input("Guess a number between 1 and 20 (inclusive): "))
#if not guess.isnumeric(): # checks if a string is only digits 0 to 9
#print("That's not a positive whole number, try again!")
while (guess!= number) and times > 1:
	if guess < 1 or guess > 20:
		print("That's not between 1 and 20. Guess again ")
		guess = int(input("Guess a number between 1 and 20 (inclusive): "))
	else:
		if (guess > number):
			print("That's too high! You have", (times - 1), "guesses left. Guess again ")
			times = times-1
			guess = int(input("Guess a number between 1 and 20 (inclusive): "))
			continue


#elif guess == number:
#	print("Congrats! You figured it out!")
		elif (guess < number):
			print ("That guess is too low! You have", (times - 1), "guesses left. Guess again ")
			times= times -1
			guess = int(input("Guess a number between 1 and 20 (inclusive): "))
			continue
if (guess==number):
		print("Congrats! You figured it out!")
if times == 1:
	print("You didn't guess the number in time! The number was", number)
