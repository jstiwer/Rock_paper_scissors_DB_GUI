from numpy import random
import sqlite3

conection = sqlite3.connect("C:/Users/UNSC/Downloads/Github_2023/Rock_paper_scissors_DB_GUI/DB.db")
cursor = conection.cursor()

def table_exist (RESULTS_GAME):
    cursor.execute('''SELECT count(name)
                        FROM SQLITE_MASTER 
                        WHERE TYPE = 'table' 
                        AND name = '{}'
                        '''.format(RESULTS_GAME)
                    )
    if cursor.fetchone()[0] == 1:
        return True
    else:
        cursor.execute('''CREATE TABLE RESULTS_GAME (ID INTEGER PRIMARY KEY AUTOINCREMENT, HUMAN_CHOICE TEXT, COMPUTER_CHOICE TEXT, WINNER TEXT, LOSSER TEXT)''')
        conection.commit()
        return False

def insert_commit ():
    cursor.execute('''INSERT INTO RESULTS_GAME (HUMAN_CHOICE, COMPUTER_CHOICE, WINNER, LOSSER) VALUES ('{}', '{}', '{}', '{}') '''.format(input_2, choice_computer_2, winner, losser))  
    conection.commit()

#Game logic
first_line = "Enter 'R' for rock, 'P' for paper or 'S' for scissors"
print(first_line)

play = True
correct_choices_list = ['r', 'p', 's', 'rock', 'paper', 'scissors']
play_again_list = ['y', 'n', 'yes', 'no']

def game(): 
    global input_
    input_ = (input('Rock, paper and scissors: ')).lower()
    while input_ not in correct_choices_list:
        print('Oh no! Repeat your choice')
        input_ = (input('Rock, paper and scissors: ')).lower()
    else:
            election_analysis()

def election_analysis():
    global input_
    global input_2
    global choice_computer_2

    if input_ == correct_choices_list[0] or input_ == correct_choices_list[3]:
        input_ = correct_choices_list[0]
        input_2 = correct_choices_list[3]
    elif input_ == correct_choices_list[1] or input_ == correct_choices_list[4]:
        input_ = correct_choices_list[1]
        input_2 = correct_choices_list[4]
    else:
        input_ = correct_choices_list[2]
        input_2 = correct_choices_list[5]

    #Choice of computer
    choice_ramdom = random.randint(3)
    if choice_ramdom == 0:
        choice_computer = 'r'
        choice_computer_2 = 'rock'
    elif choice_ramdom == 1:
        choice_computer = 'p'
        choice_computer_2 = 'paper'
    else:
        choice_computer = 's'
        choice_computer_2 = 'scissors'

    ##Choices
    print('Human: {} \nComputer: {}'.format(input_2.capitalize(), choice_computer_2.capitalize()))

    human_wins_b = False
    tied_b = False
    tied = 'Tied\n'
    human_wins = 'Human wins\n'
    computer_wins = 'Computer wins\n'

    #Winnner and loser
    if input_ == choice_computer:
        tied_b = True
        print (tied)
    elif input_ == 'r':
        if choice_computer == 'p':
            print(computer_wins)
        else:
            human_wins_b = True
            print(human_wins)
    elif input_ == 'p':
        if choice_computer == 'r':
            human_wins_b = True
            print(human_wins)
        else:
            print(computer_wins)
    elif input_ == 's':
        if choice_computer == 'r':
            print(computer_wins)
        else:
            human_wins_b = True
            print(human_wins)

    #who_wins():
    global winner
    winner = ''
    global losser
    losser = ''
    if tied_b == True:
        winner = 'tied'
        losser = 'tied'
    elif human_wins_b == True:
        winner = 'human'
        losser = 'computer'
    else:
        winner = 'computer'
        losser = 'human'

def play_again_function ():
    game()
    insert_commit()
    play_again = (input('Play again? Y/N: ').lower())
    while play_again not in play_again_list:
        if play_again in play_again_list:
            if play_again == play_again_list[0] or play_again == play_again_list[2]:
                return first_line
            elif play_again == play_again_list[1] or play_again == play_again_list[3]:
                global play 
                play = False
                print('Thanks for playing')
                return play
        else: 
            print('Oh no! Repeat your choice')
            play_again = (input('Play again? Y/N: ').lower())
            if play_again == play_again_list[0] or play_again == play_again_list[2]:
                return first_line
            elif play_again == play_again_list[1] or play_again == play_again_list[3]:
                play = False
                print('Thanks for playing')
                return play
    else:
        if play_again == play_again_list[0] or play_again == play_again_list[2]:
            play = True
        else:
            play = False
            print("It seems you don't want to play.\nGoodbye!")

def game_loop():
    while play == True:
        play_again_function()

table_exist('RESULTS_GAME')

game_loop()

conection.close()

