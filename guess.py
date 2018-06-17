import random

numMin = 1
numMax = 20
numRand = random.randint(1, 20)
amountTries = 6

print('Hello. What is your name?')
name = ''

while not name:
	name = input()
	if not name:
		print('Please enter a name.')

print('Well, ' + str(name) + ', I am thinking of a number between ' + str(numMin) + ' and ' + str(numMax) + '.')

for amountGuess in range(1, amountTries + 1):
	print('Take a guess.')
	
	try:
		num = int(input())

		if (num < numRand):
			print('Your guess is too low.')
		elif (num > numRand):
			print('Your guess is too high.')
		else:
			break # correct number!
	except: 
		print('You did not enter a number, please try again.')

try:
	if num == numRand:
		print('Good job, ' + name + '! You guessed my number in ' + str(amountGuess) + ' guesses!')
	else:
		print('Nope. The number I was thinking of was ' + str(numRand) + '.')
except: 
	print('You did not enter a single valid number.')