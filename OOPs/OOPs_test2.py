class Animal:
    name = " tiger "
    legs = " 4 "
    colour = " orange "

    def __init__(self, name, legs, colour):
        print("args constrcutor called")
        self.name = name
        self.legs = legs
        self.colour = colour

    def run(self):
        print(" name {} legs {} colour {} ".format(self.name,self.legs,self.colour))

    def __eq__(self, other):
        if isinstance(other, Animal):
            if other.colour == self.name and other.legs == self.legs and other.colour == self.colour:
                return True
        return False

        def __str__(self) -> str:
            return f"{self.name}({self.legs}){self.colour}"

Animal0 = Animal("lion", 4, "brown")

print("Animal",isinstance(Animal0, Animal))

#class variables
print(Animal0.__class__.name)
print(Animal0.__class__.legs)
print(Animal0.__class__.colour)

#instance variables
print(Animal.name)
print(Animal.legs)
print(Animal.colour)
Animal0.run()

Animal1 = Animal("elephant", 4,"dark grey")
Animal1.run()

print("Animal == Animal1 ",Animal == Animal1)

Animal1.name = "elephant"
Animal1.legs = 4
Animal1.colour = "brown"