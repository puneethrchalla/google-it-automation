# Class Definition & Docstrings Example

class Piglet:
    """Represents a piglet that can say their name."""
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def speak(self):
        """Outputs a message including the name of the piglet."""
        print("Oink! I'm {}! Oink!".format(self.name))

    def pig_years(self):
        """Converts the current age to equivalent pig years."""
        return self.age * 18

hamlet = Piglet("Hamlet",3)
hamlet.speak()
print(hamlet.pig_years())