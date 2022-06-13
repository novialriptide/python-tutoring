import random


class Entity:
    def __init__(self, health, attacks, heal_potions):
        self.health = health
        self.attacks = attacks
        self.heal_potions = heal_potions

    def heal(self):
        if self.heal_potions > 0:
            self.heal_potions -= 1
            self.health += 10

    def attack(self, entity):
        entity.health -= random.randint(self.attacks[0], self.attacks[1])


player = Entity(100, [5, 10], 2)
enemy = Entity(100, [2, 7], 2)

while True:
    print("---------------------------")
    print(f"Enter 1 to attack!")
    print(f"Enter 2 to heal!")
    print("")
    print(f"Player's Health | {player.health}")
    user_input = int(input("> "))

    if user_input == 1:
        print("Attacking the enemy!")
        player.attack(enemy)

    elif user_input == 2:
        print("Healing yourself!")
        player.heal()

    if enemy.health <= 0:
        print("You won")
        break

    enemy_choices = ["attack", "heal"]

    if random.choice(enemy_choices) == "attack":
        print("Enemy has struck you with an attack!")
        enemy.attack(player)

    else:
        print("Enemy has healed itself!")
        enemy.heal()

    print(f"The enemy has {enemy.health} health")

    if player.health <= 0:
        print("You lost")
        break
