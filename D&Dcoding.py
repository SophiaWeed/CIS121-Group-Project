import random   #used for random damage values in attacks

# ---- CLASS DESIGN ----*
class Character:
    def __init__(self, name, char_class, hp, attack, defense, intelligence): 
#constructor sets up a character with a name, class, and stats
        self.name = name   #character's name
        self.char_class = char_class   #characters class type(barb,wizard,cleric)
        self.hp = hp   #health points
        self.attack = attack    #attack power
        self.defense = defense   #defense power
        self.intelligence = intelligence
    def take_damage(self, dmg):
        self.hp -= dmg          #subtracts damage from hp
        if self.hp < 0:        # prevents negative hp(not possible)
            self.hp = 0
#returns true if the character is still alive
    def is_alive(self):
        return self.hp > 0
#each class has a special ability(used in battle)
    def special_ability(self):
        if self.char_class == "Barbarian":
            print(f"{self.name} enters a rage! More damage, but defense drops!")
            self.attack += 3    #increases attack power
            self.defense -= 1     #reduces defense
        elif self.char_class == "Wizard":
            print(f"{self.name} casts Fireball! Big magical damage!")
            return random.randint(6, 10)    #return random fireball damage
        elif self.char_class == "Cleric":
            print(f"{self.name} casts Cure Wounds and heals 3 HP!")
            self.hp += 3        #heals some hp
        return 0                #return 0 if no direct damage dealt
    


def puzzle_phase(player):
    print("\n--- STORY PHASE ---")
    print("You travel through the dark woods and reach a mysterious stone gate.")
    print("A glowing riddle appears on the door...")

    # 🆕 NEW CODE: Randomly generate a math problem
    num1 = random.randint(2, 10)
    num2 = random.randint(2, 10)
    answer = num1 * num2  # Correct answer

    print("\nTo open the gate, you must solve this riddle:")
    print(f"What is {num1} x {num2}?")

    # 🆕 NEW CODE: Hint system based on Intelligence stat
    if player.intelligence >= 8:
        print("Hint (Smart Wizard): You sense the answer is close to", num1 * (num2 - 1), "plus", num1)
    elif player.intelligence >= 5:
        print("Hint (Cleric): You recall multiplication is repeated addition...")
    else:
        print("Hint (Barbarian): You remember seeing a number that looked like", random.randint(5, 100))

    # 🆕 NEW CODE: 3 tries loop to solve puzzle
    for attempt in range(3):
        try:
            guess = int(input("Your answer: "))
            if guess == answer:
                print("✅ The gate opens! You solved the riddle.")
                return True  # Puzzle success
            else:
                print("❌ The door glows red... try again.")
        except ValueError:
            print("Please enter a number!")

    # 🆕 NEW CODE: Failing all attempts causes HP damage
    print("The magic rejects you! The door blasts you with energy!")
    player.take_damage(3)
    print(f"You take 3 damage. HP now {player.hp}")
    return False

# ---- FUNCTIONS ----
def choose_class():
#loop tp make sure user chooses a valid option
    while True:
        print("\nChoose your class:")
        print("1. Barbarian (High HP, High Damage, Low Intelligence)")
        print("2. Wizard (Low HP, High Magic Damage, High Intelligence)")
        print("3. Cleric (Balanced, Can Heal, Medium Intelligence)")
        choice = input("> ")  #ask for user input
    #uses selection statements(if/elif/else) to return to the chosen class
        if choice == "1":
            return "Barbarian"
        elif choice == "2":
            return "Wizard"
        elif choice == "3":
            return "Cleric"
        else:
            print("Invalid choice, try again!") #loop repeats until valid input


def battle(player, enemy):
#start the battle and display the enemy's name
    print(f"\nA wild {enemy['name']} appears!\n")
#main battle loop: runs as long as both player and enemy are still alive
    # Simple turn-based battle loop
    while player.is_alive() and enemy['hp'] > 0:
        #displays current health values
        print(f"\n{player.name}'s HP: {player.hp} | {enemy['name']}'s HP: {enemy['hp']}")
        action = input("Do you want to (A)ttack or use (S)pecial ability? ").lower()
        #if user chooses to attack
        if action == "a":
            damage = max(0, player.attack - enemy['def']) #calculate damage 
            enemy['hp'] -= damage        #reduce enemy hp
            print(f"You hit {enemy['name']} for {damage} damage!")
            #if user uses special ability
        elif action == "s":
            extra = player.special_ability()   #call class ability
            if extra:                         
                enemy['hp'] -= extra          #apply damage if ability deals any 
                print(f"Your spell hits {enemy['name']} for {extra} damage!")

        # Enemy turn, enemy atacks but only if it is still alive
        if enemy['hp'] > 0:
            enemy_damage = max(0, enemy['atk'] - player.defense)
            player.take_damage(enemy_damage)    #reduce player hp
            print(f"{enemy['name']} hits you for {enemy_damage}!")

    # Determine result(check who won)
    if player.is_alive():
        print(f"\n🎉 {player.name} defeated {enemy['name']}!") #player victory message
        return "Win"               #return result
    else:
        print(f"\n💀 {player.name} was defeated...")    #player defeat message
        return "Lose"                            #return result


def save_result(name, char_class, result):
#open file in append mode to save result at the end of the file
    with open("scores.txt", "a") as file:
        file.write(f"{name},{char_class},{result}\n")  #save as comma separated format


def show_past_scores():
    print("Previous Scores:")
    try:
        #try to open the scores file to read past results
        with open("scores.txt", "r") as file:
            for line in file:
                #split each line by comma to separate the values
                name, char_class, result = line.strip().split(",")
                print(f"{name} the {char_class}: {result}") #display each past result
    except FileNotFoundError:
        #if the file doesn't exist, tell the user
        print("No previous scores found.\n")


# ---- MAIN PROGRAM ----
def main():
    print("Welcome to Mini RPG Battle!")
    show_past_scores()  #Show previous players results first
#get the player's name
    name = input("\nEnter your character's name: ")
#let the user choose a class
    char_class = choose_class()

    # Character stats (using a dictionary)
    stats = {
        "Barbarian": (15, 5, 2, 3), #Low intelligence
        "Wizard": (8, 3, 1, 9),     #high intelligence
        "Cleric": (10, 4, 3, 6)     #medium intelligence
    }
#unpack stats for the selected class
    hp, attack, defense, intelligence = stats[char_class]
#create a character object using the chosen class and stats
    player = Character(name, char_class, hp, attack, defense, intelligence)

    # 🆕 NEW CODE: Call puzzle phase before battle
    passed_puzzle = puzzle_phase(player)

    # 🆕 NEW CODE: Check if player died during puzzle
    if not player.is_alive():
        print("\nYou are too weak to continue... Game Over.")
        save_result(name, char_class, "Lost to Puzzle")
        return

    # 🆕 NEW CODE: If puzzle passed, battle normally; if failed, harder battle
    if passed_puzzle:
        enemy = {"name": "Matt Priem", "hp": 12, "atk": 4, "def": 2}
        result = battle(player, enemy)
        save_result(name, char_class, result)
    else:
        print("\nYou stumble into the final room, weakened from the puzzle’s blast!")
        enemy = {"name": "Matt Priem", "hp": 12, "atk": 5, "def": 2}
        result = battle(player, enemy)
        save_result(name, char_class, result)

    print("\nGame Over! Your result has been saved.")


# ---- RUN THE GAME ----
if __name__ == "__main__":
    main()    #calls main() to start the program