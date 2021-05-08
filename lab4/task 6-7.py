class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)


    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
class func(Stack):
    def check(self):
        s = Stack()

        alp = Stack()
        num = Stack()
        b = Stack()

        with open("text6.txt", "r") as f:
            z = f.read()
            for i in range(len(z)):
                s.push(z[i])

        while len(s.items) > 0:
            a = s.pop()

            if a.isdigit():
                num.push(a)

            elif a.isalpha():
                alp.push(a)

            elif a != "\n" and a != " ":
                b.push(a)
        print("\nNumbers: ", end='\t')
        for i in range(num.size()):
            print(num.pop(), end='')
        print("\nLetters: ", end='\t')
        for i in range(alp.size()):
            print(alp.pop(), end='')
        print("\nSymbols: ", end='\t')
        for i in range(b.size()):
            print(b.pop(), end='')

        return("")

def search():
    s = Deque()

    numpl = Deque()
    numnm = Deque()

    with open("text7.txt", "r") as f:
        z = f.read()
        for i in range(len(z)):
            s.addFront(z[i])
    check = False
    while len(s.items) > 0:
        a = s.removeRear()
        if a == "-":
            check = True
        if check == True:
            numnm.addFront(a)
            if a == " ":
                check = False
                numpl.addFront(a)
        else:
            numpl.addFront(a)

    print("\n \nMinus: ", end='\t')
    for i in range(numnm.size()):
        print(numnm.removeRear(), end='')
    print("\nPlus: ", end='\t')
    for i in range(numpl.size()):
        print(numpl.removeRear(), end='')

if __name__ == "__main__":
    stek = func()
    stek.check()
    search()
