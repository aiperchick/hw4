class SuperHero:
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points,
catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def n(self):
        print(f'имя: {self.name}')
    def health(self):
        self.health_points *= 2
    def __str__(self):
        return f'никнейм: {self.nickname}, суперсила: {self.superpower}, здоровье: {self.health_points}'
    def __len__(self):
        return len(self.catchphrase)

a = SuperHero('амир', 'амир ака', 'телепорт', 10, 'машалааа')
a.n()
a.health()
print(a)
print(f'длинна фразы: {len(a.catchphrase)}')


class Ninja_Turtles(SuperHero):
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        SuperHero.__init__(self, name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def health(self):
        hero_h = self.health_points ** 2
        self.health_points = hero_h

    def f(self):
        self.fly = True

    def phrase(self):
        print('fly in the True_phrase')

a1 = Ninja_Turtles('Leonardo', 'Leo', 'Katana', 55, 'Pizzaaa')
a1.health()
print(a1)
print(f'Damage: {a1.damage}')
a1.f()
print(f'Fly: {a1.fly}')
a1.phrase()

class EarthHero(SuperHero):
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage = False, fly = False):
        SuperHero.__init__(self, name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def health(self):
        heroh = self.health_points ** 2
        self.health_points = heroh

    def f(self):
        self.fly = True
    def phrase(self):
        print('fly in the True_phrase')

b = EarthHero('Flora', 'Plants Princess', 'Plants', 15, 'Флора - фея растений!')
b.health()
print(b)
print(f'Damage: {b.damage}')
b.f()
print(f'Fly: {b.fly}')
b.phrase()


class Villain(Ninja_Turtles):
    monster = 'monster'

    def gen_x(self):...

    def crit(self):
        print(f'crit: {self ** 2}')

c = Villain('Nurlan', 'Kash', 'dz', 5, 'a')
print(c)
Villain.crit(a1.damage)