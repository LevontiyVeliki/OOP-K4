from random import randint
from random import random

class Soldier:
    def __init__(self):
        self.helth = 120
    def make_hit(self, enemy, rand_damage):
        enemy.helth -= 20 + rand_damage

class Wizard:
    def __init__(self):
        self.helth = 80
        self.mana = 50
    def make_spell_fire_ball(self, enemy):
        enemy.helth -= 30
        self.mana -= 20
    def make_spell_magik_missle(self, enemy):
        enemy.helth -= 15
        self.mana -= 5
    def make_rest(self):
        self.mana += 20

class Inventor:
    def __init__(self):
        self.helth = 100
        self.energy = 50
        self.cost_of_shot = 0
        self.power_of_shot = 40
    def make_shot_from_weapon(self, enemy):
        enemy.helth -= self.power_of_shot
        self.energy -= self.cost_of_shot
    def make_rest(self):
        self.energy += 15

chuse = int(input("Выберите вашего бойца: Солдат(1), Волшебник(2), Изобретатель(3)"))
if chuse == 1:
    your_fighter = Soldier()
if chuse == 2:
    your_fighter = Wizard()
if chuse == 3:
    your_fighter = Inventor()


chuse1 = int(input("Выберите вашего бойца врага: Солдат(1), Волшебник(2)"))
if chuse1 == 1:
    enemy_fighter = Soldier()
if chuse1 == 2:
    enemy_fighter = Wizard()

if chuse == 3:
    your_fighter.power_of_shot = int(input("Введите значение урона: "))
    if your_fighter.power_of_shot > 40:
        your_fighter.power_of_shot = 40
    if your_fighter.power_of_shot <= 0:
        your_fighter.power_of_shot = 1
    your_fighter.cost_of_shot = your_fighter.power_of_shot // 2

print("-----------------------------\n")

n = randint(0, 1)

while your_fighter.helth > 0 and enemy_fighter.helth > 0:

    n += randint(-20, 20) / 100
    rand_d = randint(-5, 10)
    print("!!!---("+ str(n) +")---!!!")

    if n % 2 < 1:
        if chuse == 1:
            your_fighter.make_hit(enemy_fighter, rand_d)
            print("Вы наносите удар!")
            print("<У врага остаётся " + str(enemy_fighter.helth) + " ХП>\n")
            n += 0.7
        if chuse == 2:
            flag = 0
            print("<У вас осталось: " + str(your_fighter.mana) + " маны!>")
            while flag == 0:
                move = int(input("Выберите: кастануть фаерболл (20 маны)(1), кастануть магическую ракету (5 маны)(2), отдохнуть (+20 маны)(3)"))
                if move == 1 and your_fighter.mana >= 20:
                    your_fighter.make_spell_fire_ball(enemy_fighter)
                    print("<Вы кастанули фаерболл!>")
                    print("<У врага остаётся " + str(enemy_fighter.helth) + " ХП>")
                    n += 1
                    flag = 1
                elif move == 1 and your_fighter.mana < 20:
                    print("<У вас недостаточно маны! Текущий уровень маны: " + str(your_fighter.mana) + "!>")
                    flag = 0
                elif move == 2 and your_fighter.mana >= 5:
                    your_fighter.make_spell_magik_missle(enemy_fighter)
                    print("<Вы кастанули магическую ракету!>")
                    print("<У врага остаётся " + str(enemy_fighter.helth) + " ХП>")
                    n += 0.5
                    flag = 1
                elif move == 3:
                    your_fighter.make_rest()
                    print("<Вы отдохнули!>")
                    n += 0.3
                    flag = 1
            print("<У вас осталось: " + str(your_fighter.mana) + " маны!>\n")
        if chuse == 3:
            flag = 0
            print("<У вас осталось: " + str(your_fighter.energy) + " энергии!>")
            while flag == 0:
                move = int(input("Выберите: выстрелить (1), отдохнуть (2)"))
                if move == 1 and your_fighter.energy >= your_fighter.cost_of_shot:
                    your_fighter.make_shot_from_weapon(enemy_fighter)
                    print("<Вы выстрелили!>")
                    print("<У врага остаётся " + str(enemy_fighter.helth) + " ХП>")
                    n += (your_fighter.cost_of_shot / 100 + 0.3)
                    flag = 1
                elif move == 1 and your_fighter.energy >= your_fighter.cost_of_shot:
                    print("<У вас недостаточно енергии! Текущий уровень енергии: " + str(your_fighter.energy) + "!>")
                    flag = 0
                elif move == 2:
                    your_fighter.make_rest()
                    print("<Вы восстановили энергию!>")
                    n += 0.3
                    flag = 1
            print("<У вас осталось: " + str(your_fighter.energy) + " энергии!>\n")



    elif n % 2 >= 1:
        if chuse1 == 1:
            enemy_fighter.make_hit(your_fighter, rand_d)
            print("Враг наносит удар!")
            print("<У вас остаётся " + str(your_fighter.helth) + " ХП>\n")
            n += 0.7
        if chuse1 == 2:
            flag = 0
            while flag == 0:
                if enemy_fighter.mana >= 30:
                    enemy_fighter.make_spell_fire_ball(your_fighter)
                    print("<Враг кастанул фаерболл!>")
                    print("<У вас остаётся " + str(your_fighter.helth) + " ХП>\n")
                    enemy_fighter.mana += 10
                    n += 1
                    flag = 1
                elif enemy_fighter.mana < 30:
                    enemy_fighter.make_spell_magik_missle(your_fighter)
                    print("<Враг кастанул магическую ракету!>")
                    print("<У вас остаётся " + str(your_fighter.helth) + " ХП>\n")
                    enemy_fighter.mana += 5
                    n += 0.5
                    flag = 1

print("-----------------------------")

if your_fighter.helth <= 0:
    print("Враг выиграл бой!")
if enemy_fighter.helth <= 0:
    print("Вы одержал победу")

