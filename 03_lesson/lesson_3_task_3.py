from adress import Address
from mailing import Mailing

to_adress = Address
from_adress = Address
to_adress = 423582, "Нижнекамск", "ул. Гагарина", 31, 8
from_adress = 423500, "Казань", "ул. Химическая", 16

sending = Mailing
sending(1234567890, to_adress, from_adress, 1200)

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
