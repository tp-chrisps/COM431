class Cat:
    def __init__(self, pname, pweight,pcolor):
        self.name = pname
        self.weight = pweight
        self.color = pcolor

    def eat(self, food):
        self.weight += food

    def print(self):
        print(self.name, self.weight, self.color)

    def __str__(self):
        return f"{self.name} {self.weight} {self.color}"

    def walk(self):
        if self.weight <=0:
            self.weight =- 1