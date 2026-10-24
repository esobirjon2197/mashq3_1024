# 10-m
class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def __repr__(self):
        return f"{self.brand} noutbuki, tezkor xotirasi: {self.ram} GB"


laptop1 = Laptop("Lenovo", 16)
print(laptop1)


# 11-m
class FootballPlayer:
    def __init__(self, fullname, number):
        self.fullname = fullname
        self.number = number

    def __repr__(self):
        return f"Maydondagi {self.number}-raqamli futbolchi — {self.fullname}"


player1 = FootballPlayer("Jasur Iskandarov", 10)
print(player1)


# 12-m
class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} buyurtmasi: {self.price} so'm"


food1 = Food("Osh", 30000)
print(food1)


# 13-m
class BankCard:
    def __init__(self, owner, bank):
        self.owner = owner
        self.bank = bank

    def __repr__(self):
        return f"{self.owner}ning banki — {self.bank}"


card1 = BankCard("Madina Sobirova", "Xalq banki")
print(card1)


# 14-m
class Game:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def __repr__(self):
        return f"{self.title} o'yini | Janri: {self.genre}"


game1 = Game("Minecraft", "Sandbox")
print(game1)


# 15-m
class Passport:
    def __init__(self, fullname, seria):
        self.fullname = fullname
        self.seria = seria

    def __repr__(self):
        return f"Pasport egasi: {self.fullname} | Seriya: {self.seria}"


p1 = Passport("Bunyod Shokirov", "AC 1234567")
p2 = Passport("Sarvar Xojametov", "AD 12356392")

print(p1)
print(p2)

