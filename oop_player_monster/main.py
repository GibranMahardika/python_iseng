class Player:
    def __init__(self, name, health=100, energy=100):
        self.name = name
        self.health = health
        self.energy = energy
        # print(f"player created")

    def attack(self, target, damage=1): # jika parameter monster ditaro sebelah kanan, akan terjadi eror, dikarenakan parameter damage sudah diberikan nilai, jika parameter damage tidak diberikan nilai, maka parameter monster ditaro dimana saja tidak akan eror
        target.health -= damage
        self.energy -= damage # self.energy = self.energy - damage
        print(f"{self.name} attack {damage} damage to {target.name}")
        if target.is_damaged(player_name=self.name):
            self.health -= target.damage
        
    def show_info(self):
        print(f"{self.name} health: {self.health}")
        print(f"{self.name} energy: {self.energy}")

class Monster():
    def __init__(self, name, health=500):
        self.name = name
        self.health = health
        self.health_init = self.health
        self.damage = 10
        # print("Monster Created")

    def is_damaged(self, player_name):
        print(f"{self.name} attack {self.damage} damage to {player_name}")
        return self.health < self.health_init #900

    def show_info(self):
        print(f"{self.name} health: {self.health}")
# Declaration
player1 = Player(name="Panjul")
player2 = Player(name="Joni")
basilisk = Monster(name="Basilisk", health=1000)
kapla = Monster(name="Kapla")
# print(player.__dict__)
# print(monster.__dict__)

# attack mode
print("=============== Attack Mode ===============")
player1.attack(target=basilisk, damage=20)
player2.attack(target=kapla, damage=80)
print("=============== Player 1 ===============")
player1.show_info()
print("=============== Player 2 ===============")
player2.show_info()
print("=============== Dragon Monster ===============")
basilisk.show_info()