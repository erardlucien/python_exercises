# In this loop example we see, how to use the break statement.
# when the if statement match, the for-loop "for x in range(2, n)"
# will be interrupted.
# The else statement belong to the first for-loop.
number = int(input('Set a number: \n'))
string = ''
array = []
i = 0

for n in range(2, number):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            array.append(n)
            i += 1
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

for index in range(i):
    if index % (i//2) == 0:
        string = string + str(array[index]) + '\n'
    else:
        string = string + str(array[index]) + ' '

print("This number are not prime:\n")
print(string)
