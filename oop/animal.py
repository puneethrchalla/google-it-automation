# Class Inheritence Example

class Animal:
    sound = ""
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(sound=self.sound,name=self.name))

class Piglet(Animal):
    sound = "Oink!"

class Cow(Animal):
    sound = "Moooo"

hamlet = Piglet("Hamlet")
hamlet.speak()

milky = Cow("Milky White")
milky.speak()