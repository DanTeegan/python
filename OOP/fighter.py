
class Fighter:
    def __init__(self, fname, lname, age, wins, losses, style):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.wins = wins
        self.losses = losses
        self.style = style

    def full_name(self):
        print(self.fname + " " + self.lname)


f1 = Fighter("Jon", "Jones", 32, 20, 1, "Freestyle")
f2 = Fighter("Conor", "Mcgregor", 30, 18, 4, "Boxer")
f3 = Fighter("Ryan", "Hall", 29, 16, 5, "BJJ")


f1.full_name()
f2.full_name()
f3.full_name()