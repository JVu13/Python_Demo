class Robot:
    def __init__(self, givenName, givenColor, givenWeight):
        self.name = givenName
        self.color = givenColor
        self.weight = givenWeight

    def introduce_self(self):
        print("My name is " + self.name) #this in Java

# r1 = Robot()
# r1.name = "Tome"
# r1.color = "red"
# r1.weight = 30

# r2 = Robot()
# r2.name = "Jerry"
# r2.color = "blue"
# r2.weight = 40

# r1.introduce_self()
# r2.introduce_self()

r1 = Robot("Tom","red",30)
r2 = Robot("Jerry","blue",40)

r1.introduce_self()
r2.introduce_self()