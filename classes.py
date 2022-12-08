class person:
    species = 'Homosapien'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("hello world")

    def hi(self):
      print("Hi my name is " + self.name)

Anthony = person("AnthonyT", 17)
print(Anthony.species)
print(Anthony.name)
Anthony.hi()

Monuiel = person("Monuiel", 17)
print(Monuiel.age)

# def hi(self):
#     print("Hi my name is" + self.name)

