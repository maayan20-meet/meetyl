'''
a = [5,4,6,7,3]
def list_fun():
	print(a[0])
	print(a[-1])
list_fun()
'''
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for i in a:
 	if i < 5:
 		print(i)
'''

'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

if len(a) > len(b):

	for i in a:
		for e in b:
			if i == e:
				c.append(i)

else:
	for i in b:
		for e in a:
			if i == e:
				c.append(i)
print(c)
'''

import tkinter as tk
from tkinter import simpledialog

number = int(simpledialog.askstring("input", "Please give me a number to check for prime!", parent=tk.Tk().withdraw()))



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

