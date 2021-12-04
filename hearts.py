num = int(input('Please enter a number: '))

hearts = ['♥' for i in range(num)]
#the * operator works as unpacking 
# * explode operator 
#print(*hearts, sep=' ')
print(' '.join(hearts))