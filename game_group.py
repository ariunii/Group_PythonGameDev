import attack_system, random, monsters_intents, textstuff, skill_system
from monsters import spawn_monster

#REQUIREMENTS
#1. dungeon game x
#2. player name add /
#3. stats /
#4. classes x
#5. ATTACK /
#6. defense and skill /
#7. inventory system x
#8. If die = end /
#9. game loop /
#10. menu /
#11. monster attacking /
#12. monster spawning /
#13. if kill boss = end x

#2
name = input("What is your name? ")
player = { #3
    
    "name": name.capitalize(),
    "atk": 3,
    "hp" : 100,
    "max_hp": 100, #max hp for heal
    "def" : 0,
    "mp": 20 #mp sys
    
}
#game variables
extra = 0
tired = 0

menu = ["1. Attack", "2. Defend", "3. Run", "4. Skills"]
#Added "4. skills" 

print(f"Welcome to the Dungeon! {player['name']}")

#10
def display_menu():
    for menu_item in menu:
        
        print(menu_item)
    
#9
while True:
    #maybe add shop here?

    #reset
    tired = 0

    monst_name, monst_atk, monst_hp, monst_def = spawn_monster() #12
    print(f"You have encountered a {monst_name}")
    print(f"~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    while True:
        if tired == 1: #if the monster is tired
            textstuff.tired() #skips everything
        else:
            pattern = random.randrange(1, 3) #pick a num 1-3, never plays if tired
            monsters_intents.patpat(pattern, monst_atk) #this monster intent
        display_menu()
        action = input("Select your action\n>")
        
        if action == "1":

            monst_hp = attack_system.damage_monster(monst_hp, player["atk"], monst_def, extra) #5
            if monst_hp <= 0:
                monst_hp = 0
                textstuff.defeat()
                break
            print(f"The monster has {monst_hp} hp remaining...")
            print(f"------------------------------")
        
        if action == "2":
            print("You brace for impact, increasing your defense!")
            player["def"] += 5 # Temporary defense boost

        # --- MONSTERS TURN ---
        if tired == 1:
            textstuff.rest()
            tired = 0
        else:
            if pattern == 1:
                print(f"-----------------------------")
                player["hp"] = monsters_intents.helit(player["hp"], monst_atk, player["def"])
            elif pattern == 2:
                print(f"-----------------------------")
                player["hp"] = monsters_intents.hehit(player["hp"], monst_atk, player["def"])
                tired = 1 #be tired pagod pagod

        # Reset the defense ONLY if the player defended this turn
        if action == "2":
            player["def"] -= 5

        if player["hp"] <= 0:
            player["hp"] = 0 #makes sure that it doesn't go into negatives, yeh
        print(f"Your HP has been reduced to {player["hp"]}!")
        if player["hp"] == 0:
            textstuff.ded()
            break
        print(f"------------------------------")
        print(f"------------------------------")
                    
        if action == "3": #changed from else to action 3
            print("You ran away, coward")
            print(f"------------------------------")
            break

        if action == "4": #skills 
            print(f"--- SKILLS (MP: {player['mp']}) ---")
            print("1. Heavy Strike (Cost: 5 MP)")
            print("2. Heal (Cost: 10 MP)")
            print("3. Back")
            skill_choice = input("Select a skill:\n")

            if skill_choice == "1":
                if skill_system.check_mp(player["mp"], 5):
                    player["mp"] -= 5
                    print("You swing with all your might!")
                    extra += 5 
                    monst_hp = attack_system.damage_monster(monst_hp, player["atk"], monst_def, extra)
                    extra = 0 
                else:
                    continue 
                
            elif skill_choice == "2":
                if skill_system.check_mp(player["mp"], 10):
                    player["mp"] -= 10
                    player["hp"] = skill_system.heal(player["hp"], player["max_hp"])
                    print(f"Your HP is now {player['hp']}! Remaining MP: {player['mp']}")
                else:
                    continue 
                
            elif skill_choice == "3":
                continue



    if player["hp"] <= 0: #outer loop checker
        break

#added stuff
