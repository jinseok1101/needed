#몇개나 만들지, 얼마나 길게 만들지를 치면 영어 소문자 + 대문자 + 특수기호로 양자컴퓨터 아니면 푸는데 오래걸릴 비번 만들어줌
#It creates a difficult password. It would be safe if hackers didn't use quantum computers

import string
import random

a = int(input('How many lines should I make? : '))
b = int(input('How long should I make it? : '))

for x in range(a):
	print('\n')
	print(''.join(random.SystemRandom().choice(string.digits + string.ascii_letters + string.punctuation) for _ in range(b)))

