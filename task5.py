value = input("Your Input Here:")

print(f'You entered: {value} and its type is')

if (value.isnumeric()):
	print(f'Numerical')
	quit()

if (value.isalpha()):
	print(f'Alphabetical')
	quit()

if (value.isalnum()):
	print(f'AlphaNumerical')
	quit()
