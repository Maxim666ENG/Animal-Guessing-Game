import random

class Animal:
    def __init__(self, type, color, size, speed, habitat):
        self.color = color
        self.size = size
        self.speed = speed
        self.habitat = habitat
        self.type = type

#Function that asks user if he wants to read the rules
def start():
    while True:
        request = input("Enter 'Help' to read the rules or enter 'No' to skip: ").strip().lower()  #Avoiding code breaking
        if request == 'help':
            print("You will be given 3 attempts and qualities of an animal, try to guess what animal it is.")
            break
        elif request == 'no':
            break
        else:
            print("Invalid input!")
start()


#creating animals and their characteristics
animal_tup = (('cat', 'black', 'small', 'average speed', 'household'),('lion', 'sand', 'large', 'fast', 'Savanna'))

#main game logic
def main_game():
    rand_animal = random.choice(animal_tup)    #generating randomly an animal
    animal = Animal(*rand_animal)
    attempts = 3
    while True:                                    
        print (f"Can you guess an animal that is {animal.size}, {animal.color} and lives in {animal.habitat}?") #using 'Animal' class to describe an animal
        guess_1 = input("what animal is it?: ")
        if guess_1 != animal.type:
            attempts -= 1                                        #Reducing the amount of attempts by 1 if user is wrong
            print('Wrong! ' + str(attempts) + ' attempts left')
            if attempts <= 0:
                print('You lost.')
                break
        else:
            print("You've won!")
            break
main_game()





























