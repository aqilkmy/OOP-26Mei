    # class Player:
        # attribute
    #    name = "Akbar" #public
    #  __salary = 2_000_000 #private

    #   __ -> private
    #   _  -> protected

        # method
    #  def get_salary(self):
    #      return self.__salary
    # pass

    #player = Player()
    #player.name = "Budi"
    #player.salary = 3_000_000

    #print(f"Nama : {player.name}")  
    #print(f"GajiPrivate : {player.get_salary()}")
    #print(f"GajiPublic : {player.salary}") 
import random

import sys
sys.path.append('D:\\Programming\\OOP 26Mei')
import main

import libs 
import os

def game_start():
    print("test")
    class Player:
        def __init__(self, name, health=100, energy=100):
            self.name = name
            self.health = health
            self.energy = energy
            # self.energy = energy.copy()
            #print(f"Player created")
        
        def attack(self, target, damage=1):
            target.health -= damage
            self.energy -= damage * 20 / 100 # self.energy = self.energy - damage
            self.damage = damage
            print(f"\n{self.name} deal {damage} damage to {target.name}, consume {player.energy} energy")
            if target.is_attacked(player_name=self.name):
                self.health -= target.damage
            

        def show_info_before(self):
            print(f"{self.name} health : {self.health} left")
            return(f"{self.name} energy : {self.energy} left")
            

        def show_info_after(self):
            if self.health < 0:
                return(f"{self.name} dead!")
            else:
                print(f"{self.name} health : {self.health} left")
                print(f"{self.name} energy : {self.energy} left")
            
    class Enemy:
        def __init__(self, name, health=500, damage=random.randint(1, 50)):
            self.name = name
            self.health = health
            self.health_init = self.health
            self.damage = damage
            #print(f"Enemy summoned")

        def is_attacked(self, player_name):
            print(f"{self.name} deal {self.damage} damage to {player_name}!\n ")
            return self.health < self.health_init

        def show_info(self):
        
            if self.health <= 0:
                print(f"{self.name} dead!")
                return self.health
            else:
                return(f"{self.name} health : {self.health} left")
            

        # CHARACTER
    player1 = Player(name="Balmond", health=200)
    player2 = Player(name="Layla")

        # ENEMY
    lord = Enemy(name="Lord", health=1000)
    turtle = Enemy(name="Turtle")

    while True:
        print(f"\nList character :\n1.{player1.name} \n2.{player2.name} \n")
        char = int(input("Pick character : "))
        os.system("clear")
        if char == 1:
            player = player1
            print(f"Character picked : {player.name}")
        elif char == 2:
            player = player2
            print(f"Character picked : {player.name}")
        else: char = int(input(f"Please pick an available character : "))

        while char!=1 and char!=2:
            char = int(input(f"Please pick an available character : "))

        confirm_answer = str(input(f"\nAttacking? [y/n]: "))

        if confirm_answer == "n":
            print("You surended [Defeat]")
            menu()
        elif confirm_answer == "y":
            print(f"\nAttack target :\n1.Lord \n2.Turtle \n")
            enemy_target = int(input(f"Choose target : "))
        while confirm_answer !="n" and confirm_answer !="y" and confirm_answer==int():
            confirm_answer = str(input(f"Please confim answer! : "))

        os.system("clear")

        if enemy_target == 1:
            target_choose=lord
            print(f"Target : {target_choose.name}")
        elif enemy_target == 2:
            target_choose=turtle
            print(f"Target : {target_choose.name}")
        else: enemy_target = int(input(f"Please choose available target : "))

        while enemy_target!=1 and enemy_target!=2:
            enemy_target = int(input(f"Please choose available target : "))

        os.system("clear")

        if player == player1:
            print(player.show_info_before())
            player.damage = int(input(f"\n{player.name} damage : "))
            if player.energy <= player.damage:
                health_decreased = (player.damage - player.energy) * 10 / 100
                player.health -= health_decreased
                print(f"Extra energy required! \nHealth consumed for energy : {health_decreased}")
            player.attack(target=target_choose, damage=player.damage)
            player.show_info_after()
            target_choose.show_info()

        elif player == player2:
            print(player.show_info_before())
            player.damage = int(input(f"{player.name} damage : "))
            if player.energy <= player.damage:
                health_decreased = (player.damage - player.energy) * 10 / 100
                player.health -= health_decreased
                print(f"Extra energy required! \nHealth consumed for energy : {health_decreased}")
            player.attack(target=target_choose, damage=player.damage)
            print(f"\n{player.show_info_after()}")
            print(f"\n{target_choose.show_info()}")

        else:
            print("Restart program")
            menu()


        if player.health <= 0:
            print(f"{player.name} dead! [Defeat]")
            return player.health
            menu()
        elif target_choose.health <= 0:
            print(f"{target_choose.name} dead! [Victory]")
            return target_choose.health
            menu()
        else:
            continue_attack = input(f"\nContinue attack? [y/n]")
            if continue_attack == "n":
                break
        
if __name__ == '__main__':
    game_start()

