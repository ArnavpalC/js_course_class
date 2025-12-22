class student:
    grade = 7
    name = 'arnav'

    def introduction(self):
        print('hi i am a student')

    def details(self):
        print('my grade is', self.grade)
        print('my name is', self.name)

ob = student()
ob.introduction()
ob.details()
