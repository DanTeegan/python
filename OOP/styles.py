from fighter import Fighter

class Style(Fighter):

    def __init__(self, fname, lname, age, wins, losses, boxer, bjj, muay_thai):
        super().__init__(fname, lname, age, wins, losses)
        self.boxer = boxer
        self.bjj = bjj
        self.muay_thai = muay_thai



a = Style("Jorge", "Masvidal", 33, 32, 7, True, True, True )
# a.what_style()
print(a)