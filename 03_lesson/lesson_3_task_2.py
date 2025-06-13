from smartphone import Smartphone

catalog = [
    Smartphone(brand: "Apple", model: "14pro", number:"+79270448857"),
    Smartphone(brand: "Lenovo", model: "12", number:"+79064587952"),
    Smartphone(brand: "Honor", model: "30i", number:"+79050000000"),
    Smartphone(brand: "Samsung", model: "M31S", number:"+79390362555"),
    Smartphone(brand: "Techno", model: "524", number: "+79112224433"),
]
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}.")