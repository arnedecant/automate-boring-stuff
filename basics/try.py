def divide(number):
	try:
		return 42 / number
	except ZeroDivisionError:
		print('Error: you tried to divide by zero.')

print(divide(2))
print(divide(12))
print(divide(0))
print(divide(1))
print('---')

print('How many dogs do you have?')
numDogs = input()
try:
	if (int(numDogs) >= 4):
		print('That is a lot of dogs.')
	elif (int(numDogs) < 0):
		print('You cannot have a negative amount of dogs.')
	else:
		print('Get more dogs.')
except ValueError:
	print('You did not enter a number')