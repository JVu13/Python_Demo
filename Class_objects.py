class Robot:
    def __init__(self, givenName, givenColor, givenWeight):
        self.name = givenName
        self.color = givenColor
        self.weight = givenWeight

    def introduce_self(self):
        print("My name is " + self.name) #this in Java

class Person:
    def __init__(self, n,p,i):
        self.name = n
        self.personality = p
        self.is_siting = i

    def sit_down(self):
        self.is_siting = True

    def stand_up(self):
        self.is_siting = False

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

# r1.introduce_self()
# r2.introduce_self()

p1 = Person("Alice", "agressive", False)
p2 = Person("Becky", "talkative", True)

# p1 owns r2
p1.robot_owned = r2
p2.robot_owned = r1

p1.robot_owned.introduce_self()