# homework 4

class Mother:
    def __init__(self, name):
        self.name = name

class Father:
    def __init__(self, age):
        self.age = age

class Grandma:
    def method(self):
        print('amir sleep')

class Brother:
    def method2(self):
        print('amir eat')

class Son(Mother, Father, Grandma, Brother):
    def __init__(self, name, age):
        Mother.__init__(self, name)
        Father.__init__(self, age)

a = Son('Vladick', 11)
print(a)
a.method()
a.method2()

with open('txt.file', 'w', encoding='utf-8') as file:
    file.write('команды гита: 1)git init, 2)git add, 3)git commit\n'
               '4)git status, 5)git rm, 6)git push origin, 7)git branch\n'
               '8)git config --global, 9)git checkout')
