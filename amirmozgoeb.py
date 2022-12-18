# дз Али

class Person:

    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        return f'name: {self.fullname}\n' \
               f'age: {self.age}\n' \
               f'is married: {self.is_married}'

person = Person('Aibek', 38, 'yes')
print(person)