from styles import Style

class Train(Style):

    def __init__(self, fname, lname, age, wins, losses, boxer, bjj, muay_thai, train):
        super().__init__(fname, lname, age, wins, losses, boxer, bjj, muay_thai)
        self.train = train

    def training(self):
        self.box = 0
        self.bjj = 0
        self.muay_thai = 0

        print("1 - boxing training")
        print("2 - bjj training")
        print("3 - muay thai training")
        ui = input("What would you like to train?")
        if ui == 1:
            self.box += 50
        elif ui == 2:
            self.bjj += 55
        elif ui == 3:
            self.muay_thai += 65
        print(f"You boxing is now {self.box}, your bjj is now {self.bjj}, your muay thai is now {self.muay_thai}")

training = Train("Jon", "Jones", 23, 19, 0, True, True, True, True)
training.training()