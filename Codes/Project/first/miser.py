import Boy
class Miser(Boy.Boy):
    def __init__(self,x,y,z,w):
        super().__init__(x,y)
        self.type=z
        self.country=w
    def prin(self):
        super().prin()
        print(self.type)
        print(self.country)
bo=Miser("rohan","delhi","miser","india")
bo.prin()