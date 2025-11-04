# Welcome and brief the user, ask for a character name, show blurbs of each class 
# and prompt the user to pick one.
print("\n")
print ("__Welcome! You're about to embark on a new adventure. But first, let's figure out who you are.__ \n")
char_name = str(input("Enter the name of your character: "))
confirm_name = input(f"Your character's name is {char_name}. Type 'Confirm' to continue or 'New' to change your character's name: ")

while confirm_name != "Confirm":
    if confirm_name == "New":
        while confirm_name == "New":
            char_name = str(input("Enter the name of your character: "))
            confirm_name = input(f"Your character's name is {char_name}. Type 'Confirm' to continue or 'New' to change your character's name: ")
    else:

        char_name = str(input("Enter the name of your character: "))
        confirm_name = input(f"Your character's name is {char_name}. Type 'Confirm' to continue or 'New' to change your character's name: ")

print(f"\n Hello, {char_name}!\n")
print("In this game, you'll play as a Barbarian, Wizard, or Cleric:")
print("------------------------------------------------------------------------------------------")
print("|___Class___|__Health__|_Armor_Class_|__Damage__|__Weapon__|_Intellect_|_Special_Ability_|")
print("| Barbarian |    45    |      10     |   6-10   |    Axe   |    Low    |       Rage      |")
print("|   Cleric  |    30    |      15     |    1-5   |   Sword  |   Medium  |    Cure Wounds  |")
print("|   Wizard  |    15    |       5     |    4-8   |   Staff  |    High   |     Firebabll   |")
print("------------------------------------------------------------------------------------------\n")
print("Armor Class (AC): How hard you are to hit\nDamage: The average damage done by an attack")
print("Rage: An ability that bolsters damage but sacrifices AC\nCure Wounds: Magic that restores your health\nFireball: A spell that can hit multiple opponents at once")
print("\n")
char_class = input("Choose your class: Barbarian, Cleric, or Wizard: ")
while char_class not in ["Barbarian","Cleric","Wizard"]:
    print("Invalid class entered.")
    char_class = input("Choose your class: Barbarian, Cleric, or Wizard: ")

confirm_class = input(f"You have chosen to be a {char_class}. Enter 'Confirm' to continue or 'New' to change your character's class: ")
while confirm_class != "Confirm":
    if confirm_class == "New":
        char_class = input("Choose your class: Barbarian, Cleric, or Wizard: ")
        while char_class not in ["Barbarian","Cleric","Wizard"]:
            print("Invalid class entered.")
            char_class = input("Choose your class: Barbarian, Cleric, or Wizard: ")
        confirm_class = input(f"You have chosen to be a {char_class}. Enter 'Confirm' to continue or 'New' to change your character's class: ")
    else: 
        print("Invalid class entered.")
        char_class = input("Choose your class, Barbarian, Cleric, or Wizard: ")
        confirm_class = input(f"You have chosen to be a {char_class}. Enter 'Confirm' to continue or 'New' to change your character's class: ")
print(f"\nYou are {char_name} the {char_class}.")
