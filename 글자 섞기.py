#2022 / 05 / 17

# 무려 영어든 한글이든 넣으면 섞어서 출력해줘서 비밀번호나 아이디를 일반인 코스프레 가능하게 만들어 준다. 아ㅏ 놀랍다!! 
# 예시 : llikegfriendsongs를 glgnsdirisleenkfo이런식으로 바꿀 수 있음ㅇㅇ

import random

l = list(input('섞을 것들을 넣어주세요. : '))

random.shuffle(l)

print("".join(map(str, l)))
