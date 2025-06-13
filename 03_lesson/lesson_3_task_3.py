from adress import Address
from mailing import Mailing

to_adress = Address
from_adress = Address
to_adress = 423582, "Нижнекамск", "ул. Гагарина", 31, 8
from_adress = 423500, "Казань", "ул. Химическая", 16

sending = Mailing
sending(to_adress, from_adress, 1500, 9374567890)
mailing = Mailing("25462", from_adress, to_adress, "1500")

print(mailing)
