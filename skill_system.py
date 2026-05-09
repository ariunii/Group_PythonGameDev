#GENERAL
#healing system

#defending system
    #halve damage/reduce damage to 0? (optional)

#check stats
    #check on player and enemy stats


#Different skills depending on classes? (optional)
#Either cooldown system OR mp system? (optional)
    #MP System: 
        ##Add mp variable
        ##Each turn, add a set number of mp OR attacks recover mp
        ##Choice to rest to recover mp rather than attack
        ##Skills minus mana, cannot work if BLANK < BLANK
        ##Is player mp already full at the start of the battle?
    #Cooldown System
        ##Add cooldown variable to each skill
        ##Each turn, reduce ALL cooldowns by 1
        ##Every skill needs different cooldown variable
        ##Skill cannot work unless cooldown = 0
        ##Are every skill's on cooldown at the start of the game?
#Decide if a skill ends the turn like attack (optional)

# skill_systemizations ni jerms
# healing system ito
def heal(hp, max_hp):
    heal_amount = 40
    hp += heal_amount
    if hp > max_hp:
        hp = max_hp # Para di mag overheal past max HP
    print(f"You cast Heal! You recover {heal_amount} HP.")
    return hp

# defense sys 
def defend(current_def):
    def_boost = 5
    print(f"You brace yourself! Defense increased by {def_boost} for this turn.")
    return current_def + def_boost

# MP check system
def check_mp(current_mp, cost):
    if current_mp >= cost:
        return True
    else:
        print("You don't have enough MP to cast that!")
        return False
