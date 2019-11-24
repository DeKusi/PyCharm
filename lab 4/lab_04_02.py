class Worker:
    'doc class Worker'
    count = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Worker.count += 1

    def display(self):
        print("Worker:")
        print("{} {}".format(self.name, self.surname))


w1 = Worker("Ivan", "Ivanov")
print("w1.count: ", w1.count)
w2 = Worker("Aleksi", "Petrov")
print("w2.count: ", w2.count)
print("w1.count: ", w1.count)
print("Worker.count : {} \n".format(Worker.count))
print("Worker.__name__ :", Worker.__name__)
print("Worker.__dict__:", Worker.__dict__)
print("Worker.__doc__:", Worker.__doc__)
print("Worker.__bases:", Worker.__bases__)



# 7

class Animal:
    id = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.id += 1


    def display(self):
        print("Animal id:", Animal.id)
        print("Name: ", self.name)
        print("Age: ", self.age)



Leon = Animal("Leo", 3)
Snake = Animal("Ka", 50)
Puma = Animal("Pum", 9)


Leon.display()
print()
Snake.display()
print()
Puma.display()

# 8
# Атрибут id  общий для всех объектов, поэтому при изменении его для обного из объектов, он меняетс у всех.
# Так как он изменяется при объявлении нового объекта, а вывод на экран информации об объектах мы осуществляем
# после объявления всех объектов, он у них одинаковый.

# 9

class Animal:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.count += 1
        self.id = Animal.count

    def display(self):
        print("Animal id:", self.id)
        print("Name: ", self.name)
        print("Age: ", self.age)



Leon = Animal("Leo", 3)
Snake = Animal("Ka", 50)
Puma = Animal("Pum", 9)


Leon.display()
print()
Snake.display()
print()
Puma.display()

