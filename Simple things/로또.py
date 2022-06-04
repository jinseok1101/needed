#2022 / 6 / 4

import random

c = int(input('몇개나 원하시는지? : '))
a = list(range(1, 46))

for i in range(c):
    b = random.sample(a, 6)
    print('\n',b)
