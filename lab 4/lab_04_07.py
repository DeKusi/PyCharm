class Row:
    id = 1

    #    lst = []
    def __init__(self, collection, value):
        self.collection = collection
        self.value = value
        self.id = Row.id
        # lst.append(self)
        Row.id += 1

    def pr(self):
        print("X1\tX2\t|\tF\n", self.collection, self.value)


class Table:
    rows = []

    def __init__(self, rowsNum):
        self.rowsNum = rowsNum

    def addRow(self, row):
        # print ("Я проверяю row.id", row.id, "\n Table rows", Table.rows[0].id, "\n len", len(Table.rows))

        k = 0  # Если значение этой переменной изменится, то мы поймём, что в списке уже существует строка с таким id
        for i in Table.rows:
            if i.id == row.id:
                k = 1
                print("Ошибка. Строка с таким идентификатором уже существует.")
                break
        if k == 0:
            Table.rows.append(row)

    # не понятно как должно происходить изменение строки,на что должно меняться    def setRow (self, row):

    def getRows(self, rowId):
        for i in Table.rows:
            if i.id == rowId:
                return i

    def display(self):
        #может выводить таблицу с различным количеством X
        '''print("id\tx1\tx2\t\tf(x1,x2)")
        for i in Table.rows:
            print (i.id, "\t", i.collection[0],"\t", i.collection[1], '\t|\t', i.value)'''
        print ("id", end = "\t\t") # x1\tx2\t\tf(x1,x2)
        for e in range(1, len(Table.rows) + 2):
            print ("x", e, end = "\t\t")
        print ("   F")
        for i in Table.rows:
            print (i.id,end = "\t\t")
            for j in range(0,len(i.collection)):
                print (i.collection[j],end ="\t\t")
            print ("|",end ="  ")
            print (i.value)
            #print ("\n")

# print (i.id, "\t", i.collection[0], "\t", i.collection[1], "\t|\t", i.value)



NewObject = Row([0, 1, 1], 1)
NewObject1 = Row([1, 0, 1], 0)
table = Table(2)
NewObject.pr()
table.addRow(NewObject)
table.addRow(NewObject1)
print(table.rows[0].value)
# print ("get:", table.getRows(0))
table.display()
