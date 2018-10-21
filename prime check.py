number = int(input("What number do you wish to check?"))

x = 2
done = False

while not done:
	if number%x == 0:
		done = True
		print("your number " + str(number) + " is not prime")

	else:
		x = x+1

	if x==number:
		done = True
		print("your number " + str(number) + " is prime")