################### Scope ####################

""" 
enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

print("----------------------")

#Global scope
player_health = 10
def game_over():
    def drink_health():
        #player_health = 20
        drink_health()
    print(f"player_health inside function: {player_health}")
print(player_health)
"""

game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy) #this will give an error because new_enemy is not defined in the global scope
create_enemy()

#Modifying global variables
def increase_enemies():
  global enemies
  enemies = 2
  print(f"enemies inside function: {enemies}")
increase_enemies()


enemies = 1
def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

increase_enemies()
print(f"enemies outside function: {enemies}")

