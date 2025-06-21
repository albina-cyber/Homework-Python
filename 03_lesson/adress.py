class Address:
    def __init__(self, index, city, street, home_number, apart_number):
        self.index = index
        self.city = city
        self.street = street
        self.home = home_number
        self.apart = apart_number

    def __str__(self):
        return f"{self.index}{self.city}{self.street}{self.home}{self.apart}"
