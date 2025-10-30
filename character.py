class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, other):
        if 3 < self.attack_power < 9:
            other.hp -= self.attack_power
            print(f"{self.name} attacks {other.name} for {self.attack_power} damage!")
        else:
            self.attack_power = 3
            other.hp -= self.attack_power
            print(f"{self.name} attacks {other.name} for {self.attack_power} damage!")
    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: {self.hp} HP"
