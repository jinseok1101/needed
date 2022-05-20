#2022 / 05 / 19

#소수인지 판단해줌. 근데 속도가 좀 많이 느림. 구구단하고 이거는 숫자 좀 크게하면 벤치마크 대용으로 써도 될듯ㅋㅋ 해보니 아이폰 13프로보다 m1이 몇배는 빠르네. 프로그램 차이도 있을수도?
#Enter the number you want to know and it will print out whether it is a decimal or not. CAUTION! VERY SLOW 
#I think we can use it instead of the benchmark program 

a = int(input('Enter the number you want to know : '))
b=0
for i in range(2,a):
	if a%i==0:
		b=1
		
if b==0:
	print('%s is prime number' % a)
else:
	print('%s is not prime number' % a)