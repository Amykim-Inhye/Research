class Person:
    def __init__(self, name, age, gender, edu):
        self.name = name
        self.age = age
        self.gender = gender
        self.edu = edu
    def myIntro(self):
        print("Hello my name is " + self.name)
        print('My age is', self.age)
        print("I am " + self.gender)
        print("I have done " + self.edu)
person = Person("Harry",31,"Male","Software development")
person.myIntro()