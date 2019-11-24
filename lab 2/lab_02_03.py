a = [1, 2, 3, 4, 5]
print ("a[0] :", a[0])
print("list a[0:5] :", a[0:5])
print("list a[:] :", a[:])
print("list a :", a)
print("list a[1:5] :", a[1:])
print("list a[0:4] :", a[:4])
print("Length of list a: ", len(a))

print("\nList a (by index):")
for i in range (0, len(a)):
    print (a[i], end=" ")

print ("\n")
print ("\nList a (by elements):")
for elem in a:
    print (elem, end=" ")

print ("\n")

b = []
b.append(20)
b.extend(a)
print("List b (extended): ",b)
b.insert(3, 5)
print("List b (insert element): ",b)
b.remove(5)
print("List b (remove element): ",b)
c1 = b.pop()
print("List b (pop last element): ",b)
print("c1: ",c1)
c2 = b.pop(3)
print("List b (pop 3rd element): ",b)
print("c2: ",c2)
bCopy = b.copy()
print("List b: ",b)
print("List bCopy: ",bCopy)
b.reverse()
print("List b (reversed): ",b)
b.sort(reverse=True)
print("List b (sorted): ",b)
b.clear();
print("List b (cleared): ",b)
print("\n")

# сравнение списков
a1 = [1,2,4]
a2 = [1,2,3]
print("a1 == a2: ", a1 == a2)
a1.append(-1)
print("a1 == a2: ", a1 == a2)
print("a1 > a2: ", a1 > a2)
print("a1 < a2: ", a1 < a2)
print("\n\n")

#9
list1= []
n = 10
for i in range(0, n):
    element = int(input("Введите %d элемент списка :" %i))
    list1.append(element)
list1.sort (reverse=True)
print (list1[5:10])
print("\n\n")
#10
list2 = list(list1)
print("Изначальный список list2 :", list2)
list2.reverse()
print("Изменённый список list2 :", list2)
