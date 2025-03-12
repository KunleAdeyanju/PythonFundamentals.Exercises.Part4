sequence = [0,1]

for i in range(2,31,1):
    sequence.append(sequence[i-1]+sequence[i-2])

x = int (input('Enter a number between 0 an 30\n'))

print("The " + str(x) + "'th fibonacci number is " + str(sequence[x]) )