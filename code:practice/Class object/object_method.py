class Person:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender

    def myIntro(self):
        print("Hello my gender is" +self.gender)
        print("Hello my age is", self.age)

harry = Person(36,"male")
sarrah = Person(34,"Female")

harry.myIntro()
sarrah.myIntro()