class cat:

    def __init__(self, name, color):
        self.name =name
        self.color =color
        print(f"a cat named {name} is born")
        print(f"the cat named {name} is {color} in color")

    def meow(self):
        print(f"{self.name} is saying meow meow")

    def __del__(self):
        print(f'{self.name} has run away after hearing a loud noise')

cat1 = cat('whiskers', 'white')

cat2 = cat('milo', 'grey')

cat1.meow()
cat2.meow()

print('both of them are playing together')

del cat1
del cat2

    
