# 2022 / 05 / 16

# 구구단을 넘어선 nn단! 
# 몇단 쓸지 넣고, 얼마나 길게 구하고 싶은지 쓰면 해줌
# 와! 222222같은 숫자들을 1부터 원하는 수까지 구한 값을 다 볼 수 있다고? 정말 굉장하다! 

n = int(input('Times table : '))
c = int(input('How long? : '))
print("""

⸻⸻""")
for i in range(1,c+1):
	print('\n',n,'X',i,'=', i*n)