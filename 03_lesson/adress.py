class Address:
    def __init__(self, index, city, street, home_number, apart_number):
        self.c = city
        self.s = street
        self.h = home_number
        self.an = apart_number

    def __str__(self):
        return f"{self.c} {self.s}{self.h} {self.an}"
