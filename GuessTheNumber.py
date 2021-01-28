import random

n = random.randint(1, 100)
count = 1
chances = 10
while 1 <= chances:
    num = int(input('Guess the number:'))
    if num > n:
        print ('Lower')
    elif num < n:
        print ('Higher')
    else:
        print ('You win')
        print (count, 'Chances you took')
        break
    count += 1
