
import random


#Class used by player
class Character:
    #Construts players name, health, and damage
    def __init__(self, name, hp, damage):
        self.name = name 
        self.hp = hp 
        self.damage = damage
        self.previous_answers = []

    # Getter and Setter for name, damage, hp(health points), and previous answers
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name

    def get_hp(self):
        return self.hp
    
    def set_hp(self, new_hp):
        self.hp = new_hp

    def get_damage(self):
        return self.damage
    
    def set_damage(self, new_damage):
        self.damage = new_damage
        

    #Create alive status to know if character is alive

    def is_alive(self):
        return self.hp > 0
    
    #Create a way for character to deal damage
    
    def attack(self, enemy):

        #damage is dealt
        enemy.hp -= self.damage
        #prints the result
        print(f'{self.name} attacks {enemy.name} for {self.damage} damage')
        print(f'{enemy.get_name()} is at {enemy.get_hp()} hp')
    
    


#Creates seperate class for monster so it can attack differently using questions

class Monsters(Character): #Monster class inherits Character class methods and variables

    #imports questions answer pairs from a txt file into dictionary where question is key and answer is value
    def create_question_dict(self):
        
        with open("Questions.txt","r") as file:
            questions_dict = {}
            for line in file:
                parts = line.strip().split(",")
                if line:
                    line = line.split(",")
        # question_file = open("Questions.txt","r")
        # data = question_file.readlines()
        # for line in data:
        #     line_data = line.split(",")
            question = line[0]
            answer = line[1]
            questions_dict[question] = answer
        return questions_dict
    
    #Creates list of keys in questions_dictonary and returns a random key from that list  
    def return_random_question(self, questions_dict):
        return random.choice(list(questions_dict.keys()))

            
    
    
    # Monster gives question to player.
    #If player answers correctly they deal damage to monster. If they answer incorrectly monster deals damage to them.
    def give_question(self, player): 
        #Creates dicitionary with questions as keys and answers as values.
        #Then it picks a random question and its corresponding answer from that dictionary.
        questions_dict = self.create_question_dict()
        question = self.return_random_question(questions_dict) 
        answer = questions_dict[question]
        print(question)
    #enemy answers question and if it is incorrect they take attack damage
        player_answer = input("What is your answer? ") 
        while player_answer != answer:
            self.attack(player)
            print(question)
            player_answer = input("What is your answer? ")
             
        else:
            player.attack(self)



#create class for different steps of the game
class Game:
    #starts the game and its variable
    def __init__(self):
        self.game_running = True
    
    #Game start, story, and combat introduction.
    def start1(self):
        print("--------------------------------------------------------")
        print("__________Ctrl+Alt+Defeat: The Final Commit_____________")
        print('An adventure by Nathan Lang, Eric Nuno, and Sophia Weed')
        print("--------------------------------------------------------\n")
        print("    It's snowing outside. Students everywhere are huddled inside,")
        print("sheltering by their laptops and notebooks. There's an air of panic")
        print("in the undercurrent of staff and students alike, and you're all too")
        print("familiar with the reason: It's Finals Week at MSU Mankato.\n")
        print("Worse, it's Finals Week, and you have an 'F' in your CIS 121 course.\n")
    def start2(self):
        print("\nYou walk alone through the cold snow toward the office of Dr. Priem,")
        print("preparing yourself to beg for mercy. After entering Wissink Hall, you")
        print("are surprised to see Matt's office door swing open by itself before you")
        print("even touched the handle. The room is dark.")
        print(f"A voice comes from inside. 'Ah, I've been expecting you, {Player.get_name()}.'\n")
        input("Response: ")
        print("\nUpon closer inspection, you find Matt facing the opposite wall, reclining")
        print("in a leather swivel chair. He doesn't turn to face you.\n")
        print("    'I suppose you're wondering what you can do to pass my course,' Dr.")
        print("Priem presumed in a foreboding voice. 'Yes?'\n")
        user_ans = input("Answer 'Yes' or 'No': ")
        if user_ans != 'Yes' and user_ans != 'No':
            print("The CIS professor gives you a strange look.")
        print("    'I can see that you are. You have the look about you of desperation...'")
        print("A few moments of awkward silence followed.")
        print("At last, Matt turned and stood from the swivel chair in one fluid motion,")
        print("placing both hands on his desk with an unnerving smile.")
        print("     'Very well... I'll grant you an opportunity to improve your grade.'\n")
        input("Response: ")
        print("\n    'All you have to do is demonstrate mastery over the standards of this")
        print("course,' he continued, but his tone was strangely foreboding.")
        print("Matt raised one hand, and from the shadows, Nahili Ansha stepped forward.")
        print("     'Show me what you've learned... or FAIL!' Matt shouted, and Nahili advanced.")
    def combat_start(self):
        print("\n-------------------------------------------------------------------------------------")
        print("Nahili closes in! Answer each of her CIS 121 questions correctly to deal damage, but")
        print("beware the consequences of an incorrect answer!")
        print("-------------------------------------------------------------------------------------")
        


    # Defines the steps of the Boss fight
    def boss_fight(self, Player, Monster): #Takes input of the player and Monster that are fighting
        print(f'I {Monster.get_name()} will defeat you!!')
        #Monster and Player fight until is_alive returns False(One dies)

        while Player.is_alive() and Monster.is_alive():
            Monster.give_question(Player)
               
        if Player.is_alive():
            print('You defeated the Monster')
        elif Monster.is_alive():
            print('You were defeated')
            self.game_running = False #If player.is_alive returns false game ends

    def end(self, Player):

        if Player.is_alive():
            print('You won')
        else:
            print('Good luck next time')
        self.game_running = False




#Name Creation function
def choose_name():
    confirm_name = "New"
    player_name = ''
    while confirm_name == "New":
        player_name = input("What name do you read from your MAVCard as you leave your dorm? ")
        confirm_name = input(f"Your name is {player_name}. Enter any key to confirm or 'New' to change your name: ")
    return player_name




monsters_list = []
with open("Monster.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            name, health, attack = line.split(",")

            health = int(health)
            attack = int(attack)

            monsters_list.append(Monsters(name, health, attack))

#Function that loads questions into a dictionary to be used by monster method

game = Game()
game.start1()
# Create Character 
Player = Character(choose_name(), 20, 5)
game.start2()
game.combat_start()
for monster in monsters_list:
    if game.game_running:
        game.boss_fight(Player, monster)
    
game.end(Player)

