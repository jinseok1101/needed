# 2022 / 6 / 20 ~ 미완
# 여러개의 로또 랜덤 번호를 뽑고, 각 숫자들이 몇번이나 나왔는지를 알려주는 것

import random

c = int(input('몇개나 원하시는지? : '))
a = list(range(1, 46))

for i in range(c):
    b = random.sample(a, 6)
    print('\n',b)


