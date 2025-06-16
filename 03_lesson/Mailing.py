from adress import Address


class Mailing:
    to_address = Address
    from_address = Address
    cost = "100"
    track = "0987654321"

    def __init__(self, to_adress, from_adress, cost, track):
        self.to_adress = to_adress
        self.from_adress = from_adress
        self.cost = cost
        self.track = track

    def to_adress(self):
        print(self.to_adress)

    def from_adress(self):
        print(self.from_adress)
