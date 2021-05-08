class Deque:
    def __init__(self,name,name2):
        self.infile = name
        self.outfile = name2
        self.items = ""
        self.text = ""
        self.alf = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                    'n','o','p','q','r','s','t','u','v','w','x','y','z']
    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items += (self.alf[item])

    def removeRear(self):
        self.text = self.text[:0] + self.text[0+1:]
        return self.text

    def size(self):
        return len(self.items)

class Main(Deque):
    def decryption(self):
        with open(self.infile, "r") as f:
            self.text = f.read()
            size = len(self.text)-1
            while Deque.size(self)-1 != size:
                if self.text[0] != " ":
                    if self.text[0] != ",":
                        if self.alf[self.alf.index(self.text[0])] != self.alf[len(self.alf)-2] \
                                and self.alf[self.alf.index(self.text[0])] != self.alf[len(self.alf)-1]:
                            u = self.alf.index(self.text[0])
                            Deque.addFront(self,u+2)
                            Deque.removeRear(self)
                        else:
                            if self.alf[self.alf.index(self.text[0])] == self.alf[len(self.alf)-2]:
                                Deque.addFront(self,0)
                                Deque.removeRear(self)
                            else:
                                Deque.addFront(self, 1)
                                Deque.removeRear(self)
                    else:
                            self.items += ","
                            Deque.removeRear(self)
                else:
                    if Deque.isEmpty(self) == False:
                        if self.text[0] == " ":
                            self.items += " "
                            Deque.removeRear(self)

        return self.items

    def isClose(self):
        # проверка на пустоту входного файла
        if Deque.isEmpty(self) == False:
            with open(self.outfile, "w") as o:
                    o.write(str(self.items) + '\n')


if __name__ == "__main__":
    Kn = Main('text2.txt','out2.txt')
    Kn.decryption()
    Kn.isClose()

