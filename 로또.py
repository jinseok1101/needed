#2022 / 6 / 4

# 몇개나 추천 받을지를 적으면 그 숫자만큼 추천해줌
# 그 중 이거다 싶은걸 쓰면 됨ㅇㅇ (로또도 일단은 도박임. 차라리 그 돈으로 주식이나 코인 소숫점으로 구매하든 하는게 이득이지 않을려나 싶긴 함)

import random

c = int(input('몇개나 원하시는지? : '))
a = list(range(1, 46))

for i in range(c):
    b = random.sample(a, 6)
    print('\n',b)
