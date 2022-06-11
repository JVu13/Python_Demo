class Robot:
    def introduce_self(self):
        print("My name is " + self.name) #this in Java

r1 = Robot()
r1.name = "Tome"
r1.color = "red"
r1.weight = 30

r2 = Robot()
r2.name = "Jerry"
r2.color = "blue"
r2.weight = 40

r1.introduce_self()
r2.introduce_self()