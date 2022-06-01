#2022 / 05 / 21 ~ 미완

import webbrowser
print("""coin info = a
stock info = b
school lunch = c
Gmail = d
news = e""")

a = "https://coinmarketcap.com/ko/"
b = 'https://markets.hankyung.com/consensus'
c = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=구일고+급식'

a11 = int(input('How many do you want to go in? (1~5) : '))
#b1 = [input('어디에 들어가고 싶니? : ') for _ in range(a11)]
#if a11==1:
    #a1111 = [(input('어디에 들어가고 싶니? : ') for _ in range(1))]
    #a1111 = str('2')
    #webbrowser.open("%s" %a1111)

if a11==1:
    a1111 = [input('어디에 들어가고 싶니? : ') for _ in range(1)]

if a == a1111:
    webbrowser.open("%s" %a)
if a1111 == b:
    webbrowser.open(b)
if a1111 == c:
    webbrowser.open('%s' %c)


if a11==2:
    a111,a112 = [input('어디에 들어가고 싶니? : ') for _ in range(2)]
    webbrowser.open('%s' %a111) and webbrowser.open('https://%s' %a112)
