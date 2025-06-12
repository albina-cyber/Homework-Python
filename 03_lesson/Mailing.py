from adress import Address


class Mailing:
    to_adress = Address
    from_adress = Address
    cost = "1200"
    track = "1234567890"

    def __init__(self, to_adress, from_adress, cost, track):
        self.t = to_adress
        self.f = from_adress
        self.c = cost
        self.t = track

    def to_address(self):
        print(self.to_adress)

    def from_adress(self):
        print(self.from_adress)
