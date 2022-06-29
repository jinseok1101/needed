# 2022 / 05 / 18

# 몇개나 만들지, 얼마나 길게 만들지를 치면 영어 소문자 + 대문자 + 특수기호로 양자컴퓨터 아니면 푸는데 오래걸릴 것 같은 비번(들)을 만들어줌. 그 중 이거다! 싶은걸로 선택해서 쓰셈
# {어차피 삼성이나 애플, 웨일, 크롬 등이면 자동으로(안되거나 원하면 수동) 비번이랑 아이디 저장해주고 자동 완성 됨. 수동으로 했으면 모든 비밀번호 쭉 나오는데서 복사 가능이라 다시 칠 걱정도 그닥 없음}

import string
import random

a = int(input('몇개나? : '))
b = int(input('얼마나 길게 : '))

for x in range(a):
	print('\n')
	print(''.join(random.SystemRandom().choice(string.digits + string.ascii_letters + string.punctuation) for _ in range(b)))

