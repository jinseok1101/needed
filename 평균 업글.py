# 2022 / 5 / 30 ~ 6 / 2

# 평균 구하는건데 마지막에 나눌 수를 생각 안해도 되게 만든거
# 값들을 넣고, 엔터치면서 넣어야 할 것들을 다 넣고 end를 적고, 엔터 눌러주면 소수점까지해서 평균이 나옴
# 전에 만들었던건 뭘로 나눠야하는지를 미리 넣어야 해서 계산기만 못했는데 이건 쓸만한듯

b = []
while True:
	if ('end') in b:
		b.remove('end')
		c = list(map(int, b))
		print(sum(c)/len(c))
		break
	else:
		s = input('평균은 : ')
		b.append(s)
		

