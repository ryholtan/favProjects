# my word game, let's call it 'Le Word'


# for my categories of "secret words"
import random

# made a loop so if one wants to play with a different category and word, they can
keep_playing = True
while keep_playing is True:
# introduction
    print()
    print("""Welcome to the word guessing game! --Le Word--
    
Make sure to look for your hints! 
(an underscore means a letter in that spot, a lowercase letter means right 
letter but wrong position, an uppercase letter means right letter and right position!)""")
    print()

    # ask user for preferred category
    print("""Please pick a category.""")
    category = input("Animals, Vehicles, or People ").lower()

    # categories
    animals = ["lion", "tiger", "bear", "horse", "platipus", "fox"]
    vehicles = ["plane", "train", "bus", "truck", "forklift", "soapboxcar"]
    people = ["nelson", "young", "moroni", "isaiah", "reuben", "amy"]

    # secret random category option
    randomcat = ["animals", "vehicles", "people", "animals", "vehicles", "people"]

    # user must pick a category to play
    while category != "animals" and category != "vehicles" and category != "people" and category != "random":# secret
        category = input("Animals, Vehicles, or People ").lower()
    

    # depending on the user's choice, we will use a random word belonging to that category
    if category == "animals":
        random.shuffle(animals)
        for index in animals:
            secret = animals[0]
    elif category == "vehicles":
        random.shuffle(vehicles)
        for index in vehicles:
            secret = vehicles[0]
    elif category == "people":
        random.shuffle(people)
        for index in people:
            secret = people[0]

    # if they choose the secret randomizer
    elif category == "random":
        random.shuffle(randomcat)
        for index in randomcat:
            category = randomcat[0]
      
        if category == "animals":
            random.shuffle(animals)
            for index in animals:
                secret = animals[0]
        elif category == "vehicles":
            random.shuffle(vehicles)
            for index in vehicles:
                secret = vehicles[0]
        elif category == "people":
            random.shuffle(people)
            for index in people:
                secret = people[0]
    

    print()
    # print the length of the secret word in underscores
    guess = len(secret) * ("_ ")

    # begin our tracking of the amount of guesses the user makes
    count = 0

    # our hint generator
    while guess != secret:
        print()
        print("Your hint is: ", end="")
       
       # if they got the right letter in the right place, that letter should be capitalized
       # if they got the right letter but wrong place, that letter should be lowercase
       # any other letters will appear as an underscore
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                print(guess[i].upper(), end="")
            elif guess[i] in secret:
                print(guess[i].lower(), end="")
            else:
                print("_", end="")
        print("")
        
        # they need to make their first (and subsequent) guesses
        guess = input("What is your guess? ").lower()

        

        # if their guess doesn't have the same numeber of characters as the secret word
        # they need to correct that until they do.
        while len(guess) != len(secret):
            print("Please input the same number of characters as you see underscores.")
            print()
            guess = input("What is your guess? ")

            # add to the running count of guesses even if the number of characters is wrong
            count = count + 1

        
        # kinda redundant but they will be told if their guess was not correct.
        if guess != secret:
            print("Your guess was not correct.")
        
        # add to the running count of guesses
        count = count + 1


    # when they get the right word, they get a congrats and are told how many guesses they had
    print("Congratulations! You guessed it!")
    if count == 1:
        print(f"It took you {count} guess!!")
    else:
        print(f"It took you {count} guesses!")
    

    # the user is asked to play again, if so, the whole thing will loop
    # if not, the program will stop.
    play_again = input("Would you like to play again?(y/n) ").lower()
    if play_again == "yes" or play_again == "y":
        keep_playing = True
    else:
        keep_playing = False
print()        
print("Thanks for playing!!")
print()