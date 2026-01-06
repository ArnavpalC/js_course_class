from abc import ABC, abstractmethod



class Animal(ABC):
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print('i can walk and speak')



class Snake(Animal):
    def move(self):
        print('i can slither and snarl')



class Cat(Animal):
    def move(self):
        print('i can walk, jump and sleep')


class Penguin(Animal):
    def move(self):
        print('i can waddle around and swim')


h = Human()

s = Snake()

c = Cat()

p = Penguin()

for i in(h, s, c, p):
    i.move()
