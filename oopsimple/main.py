
class Country:
    def __init__(self, name):
        self.name = name
        self.population = 0

    def setPopulation(self, population):
        self.population = population

    def getPopulation(self):
        return self.population


class Russia(Country):
    def __init__(self):
        super().__init__("Russia")


class Canada(Country):
    def __init__(self):
        super().__init__("Canada")


class Germany(Country):
    def __init__(self):
        super().__init__("Germany")


# Test
russia = Russia()
russia.setPopulation(146_000_000)

canada = Canada()
canada.setPopulation(38_000_000)

germany = Germany()
germany.setPopulation(83_000_000)

print(russia.name, russia.getPopulation())
print(canada.name, canada.getPopulation())
print(germany.name, germany.getPopulation())