#무려 영어든 한글이든 넣으면 섞어서 출력해줘서 비밀번호나 아이디를 일반인 코스프레 가능하게 만들어 준다. 아ㅏ 놀랍다!! 예시 : llikegfriendsongs를 glgnsdirisleenkfo이런식으로 바꿀 수 있음ㅇㅇ
#If you put in the words, they are mixed and printed out. So you can make an ID and password that are not obvious with meaningful words.
#If you were an otaku{geek(?)}, you'd want this.

import random

l = list(input('Please enter words to mix : '))

random.shuffle(l)

print("".join(map(str, l)))
