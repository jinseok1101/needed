#2022 / 5 / 30 ~ 6 / 2

#평균 구하는건데 넣을 숫자가 총 몇갠지 모를 상황에서 쓸 수 있게 업글한거

b = []
while True:
	if ('end') in b:
		b.remove('end')
		c = list(map(int, b))
		print(sum(c)/len(c))
		break
	else:
		s = input('ghgyguygy : ')
		b.append(s)
		

