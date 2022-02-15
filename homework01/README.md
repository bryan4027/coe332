# This folder belongs to Bryan Acosta's homework 1.
# Eid ba25389. TACC id: ba25389.

I did the first two exercised.

Exercise 1:

Task: Create a list of ~10 different integers. Write a function (using modulus and conditionals) to determine if each integer is even or odd. Print to screen each digit followed by the word ‘even’ or ‘odd’ as appropriate.

Solution: 
1: this imports the numpy python package i use to creat my arrays and append those arrays
2: declares the vector
5: this for loop runs through every number in the vector
6 & 13: these if statements test if the value is even or odd, respectively
7 & 14: these if statements test if the first value found is the first even or odd to declare each vector
11 & 18: these lines append the current value at i onto the end of each vector
19 - 23: these print each vector


Exercise 2:

Task: Using nested for loops and if statements, write a program that iterates over every integer from 3 to 100 (inclusive) and prints out the number only if it is a prime number.

Solution:
1: I used the numpy python package to create my arrays and append the arrays later on.
2: I created a list to define the vector from 3 - 100
5: The for loop ranged from 0 to the end of the input vector
7: This for loop ranges from 2 until the value of the number being tested - it essentially test\
s that the number tested is tested by every number possible and divide the two.
9: the modulo function divides the two numbers and tells you if there is a leftover number then\ that means the number did not divide nicely; thus it is a prime
10: if statement tests the result from the modulo operation and to ensure that it ignores when \
the number divides by itself
14: this statement checks to see if the current value at allvals[i] is the first prime number t\
o be found, so it can initialize the vector
18: this is the statement that appends the current value at i onto the vector listing the prime\
s.
23-24: this prints the array.