class Character:
    def __init__(self, race, health, weapon, clothing):
        self.race = race
        self.health = health
        self.weapon = weapon
        self.clothing = clothing

    def treat(self):
        return 'Health restored'

    def pick_up_inventory(self):
        return  'Item added to bag'

    def trow_away_inventory(self):
        return 'Item dropped'

    def battle(self):
        return 'Long live the king _'

class Warrior(Character):

    def __init__(self, race, health, weapon, clothing):
        super().__init__(race, health, weapon, clothing)
        self.__weapon = weapon

    def battle(self):
        return f'Released an{self.__weapon}'

    def get_weapon(self):
        return f'My weapon is {self.__weapon}'

    def change_weapon(self):
        return f'Weapon chenged to {self.__weapon}'

class Mage(Character):
    def __init__(self, race, health, weapon, clothing, magic):
        super().__init__(race, health, weapon, clothing)
        self.magic = magic

    def treat_with_magic(self):
        return f'Health restored instantly'

    def battle(self):
        return f'Released an {self.weapon}'

class Smith(Character):
    def __init__(self, race, health, weapon, clothing, stone):
        super().__init__(race, health, weapon, clothing,)
        self.stone = stone

    def craft_a_weapon(self):
        return f'Weapon ready for battle' if self.stone >= 100 else 'Not enough stones to craft weapons'

    def battle(self):
        return f'Hit with a {self.weapon}'


Aragorn = Warrior('Human', '100', 'sword', 'armor')
print('Aragorn')
# Aragorn.weapon = 'club'
# print('Aragorn`s weapon: ', Aragorn.weapon)
# print('Get a weapon: ', Aragorn.get_weapon())
# print('Use healing: ', Aragorn.treat())
# print('Pick up item: ', Aragorn.pick_up_inventory())
# print('The battle :', Aragorn.battle())
# print('Change weapons: ', Aragorn.change_weapon('club'))
# print('Get a weapon: ', Aragorn.get_weapon())
# print('The battle:', Aragorn.battle())
# print(Aragorn.__dict__)

# Galadriel = Mage('Elf', '200', 'bow', 'cloak', 'flame levitation')
# print('Galadriel')
# print('Use healing: ', Galadriel.treat())
# print('Pick up item: ', Galadriel.pick_up_inventory())
# print('Use magic: ', Galadriel.magic)
# print('Use magic healing: ', Galadriel.treat_with_magic())
# print('The battle: ', Galadriel.battle())

print()
Gimli = Smith('Dwarf', 150, 'axe', 'armor', 125)
print(Gimli)
print('Use healing: ', Gimli.treat())
print('Pick up item: ', Gimli.trow_away_inventory())
print('Number of stones: ', Gimli.stone())
print('Craft weapon: ', Gimli.craft_a_weapon())
print('The battle: ', Gimli.battle())

