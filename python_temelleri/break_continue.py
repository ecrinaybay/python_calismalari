name = 'Sadık Turan'
'''
for letter in name:
    if letter == 'a':
        break
    print(letter)

for letter in name:
    if letter == 'a':
        continue
    print(letter)

x = 0
while x < 5:
    x+1
    if x == 2:
        continue
    print(x)
    x+=1
'''

# 1- 100 'e kadar tek sayıların toplamı

x = 0
result = 0

while x <= 100:
    x+=1
    if x%2 == 1:
        continue
    result += x

print(f'Toplam: {result}')

