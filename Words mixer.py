import random

l = list(input('Please enter words to mix : '))

random.shuffle(l)

print("".join(map(str, l)))
