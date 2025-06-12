from adress import Address
from Mailing import Mailing

to_adress = Address
from_adress = Address
to_adress = 423582, "г. Нижнекамск", "ул. Гагарина", 31, 8
from_adress = 423500, "г. Казань", "ул. Химическая", 16

sending = Mailing
sending(to_adress, from_adress, 1200, 1234567890)

print(
    "Отправление",
    sending.track,
    "из",
    from_adress,
    "в",
    to_adress,
    ". Стоимость",
    sending.cost,
    "рублей.",
)
