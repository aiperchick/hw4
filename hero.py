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
        hero_h = self.health_points * 2
        print(f'удвоеннное здоровье: {hero_h}')
    def __str__(self):
        return f'никнейм: {self.nickname}, суперсила: {self.superpower}, здоровье: {self.health_points}'
    def __len__(self):
        return len(self.catchphrase)

a = SuperHero('амир', 'амир ака', 'телепорт', 10, 'машалааа')
a.n()
print(a)
a.health()
print(f'длинна фразы: {len(a.catchphrase)}')