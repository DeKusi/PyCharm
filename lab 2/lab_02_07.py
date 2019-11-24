s = input("Введите двенадцатиричное число :")
s = int(s, 12)
p = ''
while s > 0:
    res = s % 14
    if res == 10:
        res = 'A'
    if res == 11:
        res = 'B'
    if res == 12:
        res = 'C'
    if res == 13:
        res = 'D'
    res = str(res)
    p = p+res
    s //= 14
print (p)

