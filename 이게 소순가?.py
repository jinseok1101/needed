# 2022 / 05 / 19

# 알고싶은 숫자를 넣으면 소수인지 판단해줌. 근데 속도가 좀 많이 느림. 숫자 좀 크게하면 거의 벤치마크 대용으로 써도 될듯ㅋㅋ

a = int(input('Enter the number you want to know : '))
b=0
for i in range(2,a):
	if a%i==0:
		b=1
		
if b==0:
	print('%s is prime number' % a)
else:
	print('%s is not prime number' % a)