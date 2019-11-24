import time


class Ticket:
    def __init__(self, date, name, deadline):
        self.createDate = date
        self.owner = name
        self.deadline = deadline

    def __del__(self):
        print("Delete ticket: ", time.asctime(self.createDate))

    def display(self):
        print("Ticket:")
        print(" createDate: ", time.asctime(self.createDate))
        print(" owner: ", self.owner)
        print(" deadline: ", time.asctime(self.deadline))


ticket1 = Ticket(time.localtime(), "Ivan Ivanov",
                 time.strptime("17.12.2017", "%d.%m.%Y"))
ticket1.display()
print("Owner: ", ticket1.owner)
print("Owner(getattr): ", getattr(ticket1, "owner"))
print("hasattr: ", hasattr(ticket1, "owner"))
setattr(ticket1, "owner", "Alexei Petrov")
print("Owner(setattr): ", ticket1.owner)

#2 
print("delattr: ", ticket1.owner)
delattr(ticket1, "owner")  # удаление значения атрибута


#3 при раскомментировании программа выдаёт ошибку, т.к. мы пытаемся вывести уже удалённый объект
#del ticket1 # удаление объекта
#print(ticket1)

#4
print("Текущее время сервера:  ", time.asctime(time.localtime()))


# 5
time1 = time.strptime("17.07.2017 10:53:00", "%d.%m.%Y %H:%M:%S") #создание объекта типа time по строке
print(time1)



