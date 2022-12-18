class Splinter:
    mutant = 'mutant'
    def __init__(self, name, hp, gun, food):
        self.name = name
        self.hp = hp
        self.gun = gun
        self.food = food

    def x(self):
        self.hp *= 3

    def __str__(self):
        return f'name: {self.name}\n' \
               f'hp: {self.hp}\n' \
               f'gun: {self.gun}\n' \
               f'food: {self.food}'


splinter = Splinter('Sensei', 10, 'palka', 'chees')
splinter.x()
print(splinter)

class Raf(Splinter):
    mutant = 'mutant'

    def __init__(self, name, hp, gun, food, color):
        super().__init__(name, hp, gun, food)
        self.color = color

    # def c(self):
    #     if self in raf:
    #         self == 'red'
    #         return True
    #     else:
    #         return False

    def x(self):
        self.hp *= 2

raf = Raf('Rafael', 2, 'gun', 'pizza', 'red')
raf.x()
# raf.c()
print(raf)






