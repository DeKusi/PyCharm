# Операции со словарями
d2 = dict(bananas=3, apples=5, oranges=2, bag="basket")
d5 = d2.copy()
print("Dict d5 copying d2 = ", d5)
# получение значения по ключу
print("Get dict value by key d5['bag']: ", d5["bag"])
print("Get dict value by key d5.get('bag'): ", d5.get('bag'))
print("Get dict keys d5.keys(): ", d5.keys())
print("Get dict values d5.values(): ", d5.values())
print("\n")
# 15
myInfo = {
    "name": "Ксения",
    "sername": "Анисимова",
    "middlename": "Алексеевна",
    "day": 7,
    "month": 2,
    "year": 2001,
    "university": "ITMO"
}
print("Get dict keys myInfo.keys(): ", myInfo.keys())
print("Get dict values myInfo.values(): ", myInfo.values())