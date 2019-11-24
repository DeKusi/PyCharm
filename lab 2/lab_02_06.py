s = input("Введите шестнадцатиричное число :")
s = int(s, 16)
if s >= 0:
    print(bin(s)[2:].zfill(8))
else:
    s *= -1
    b = bin(~s & 0xFF)[2:].zfill(8)
    c = int(b, 2)
    c += 1
    a = bin(c)[2:].zfill(8)
    print("Дополнительный код вашего числа равен :", a)