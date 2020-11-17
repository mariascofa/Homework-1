min = int(input("Введите минимальное значение счетчика:"))
max = int(input("Введите максимальное значение счетчика:"))
class Lichylnyk :
    def __init__(self, min=0, max=0):
        self.min = min
        self.max = max
        self.cur=min


    def show(self):
        print("Текущее значения-",self.cur)

    def move(self):
        if self.cur < self.max:
            self.cur = self.cur + 1
        else:
            self.cur = self.min


pt1 = Lichylnyk(min, max)
for _ in range (max-min):
    pt1.show()
    pt1.move()

print ("1st commit-dev-53")

print ("2nd commit-dev-53")

print ("3rd commit-dev")




