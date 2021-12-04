num = int(input('Please enter a number: '))

hearts = ['♥' for i in range(num)]

print(*hearts, sep=' ')