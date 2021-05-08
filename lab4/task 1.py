class Deque:
    #инициализаяция
    def __init__(self):
        self.file = []

    #проверка на пустоту
    def isEmpty(self):
        return self.file == []


class Main(Deque):
    #открытие файла
    def isOpen(self):
        # проверка на пустоту входного файла
        if Deque.isEmpty(self) == False:
            with open('text.txt', "r") as f:
                # преображения данных файла
                s = ""
                self.file = f.read()
                for i in range(len(self.file)):
                    if self.file[i] == ',':
                        s += '\n'
                    else:
                        s += self.file[i]
                b = 0
                for i in range(len(s)):
                    if s[i] == '\n':
                        self.file.append(s[b:i])
                        b = i + 1
                    if i == len(s)-1:
                        self.file.append(s[b:i+1])

                self.file = sorted(self.file)

    # закрытие файла
    def isClose(self):
        # проверка на пустоту входного файла
        if Deque.isEmpty(self) == False:
            with open('out.txt', "w") as o:
                for i in range(len(self.file)):
                    o.write(str(self.file[i])+'\n')


if __name__ == "__main__":
    Kn = Main()
    Kn.isOpen()
    Kn.isClose()

