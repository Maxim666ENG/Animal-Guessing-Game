import random
from classanimals import animal

words = ['cat', 'lion', 'turtle']

#giving characteristics to animals which will be printed after calling our 'classanimals' class
cat = animal('Black', 'small', 'average', 'domestic', 'household')
lion = animal('Sand', 'large', 'fast', 'predator', 'Savanna')
turtle = animal('dark green', 'small or average', 'extremely slow', 'sometimes domestic', 'household or sea')

#this block takes a random word from 'words' list
def word():
    global generated
    generated = random.choice(words)
word()

#This block obliges user to read the rules
def start():
    while True:
        request = input("Enter 'Help' to read the rules: ").strip().lower()  #Avoiding code breaking
        if request == 'help':
            print("You will be given 3 attempts and qualities of an animal, try to guess what animal it is.")
            break
        else:
            print("Invalid input!")
start()



# The main game block
def game():
    attempts = 3
    while True:
        if generated == 'cat':                                       #This line checks if the generated animal is cat
            print(vars(cat))                                         #Calling our class, and printing the characteristics
            guess_1 = input('What animal is it?: ').lower().strip()
            if guess_1 != 'cat':
                attempts -= 1                                        #Reducing the amount of attempts by 1 if user is wrong
                print('Wrong! ' + str(attempts) + ' attempts left')
                if attempts <= 0:
                    print('You lost.')
                    break
            else:
                print("You've won!")
                break
        #Almost the same block but for 'lion'
        elif generated == 'lion':
            print(vars(lion))
            guess_1 = input('What animal is it?: ').lower().strip()
            if guess_1 != 'lion':
                attempts -= 1
                print('Wrong! ' + str(attempts) + ' attempts left')
                if attempts <= 0:
                    print('You lost.')
                    break
            else:
                print("You've won!")
                break
        #for 'turtle'
        elif generated == 'turtle':
            print(vars(turtle))
            guess_1 = input('What animal is it?: ').lower().strip()
            if guess_1 != 'turtle':
                attempts -= 1
                print('Wrong! ' + str(attempts) + ' attempts left')
                if attempts <= 0:
                    print('You lost.')
                    break
            else:
                print("You've won!")
                break
game()

#If user lost or won, he/she will be asked to play again
while True:
    answer = input('Do you want to play again? Yes/No: ')
    answer = answer.lower().strip()
    if answer == 'yes':
        game()
        break
    elif answer == 'no' :
        print("Thank you for playing, bye!")
        break
    print('Invalid input')




























