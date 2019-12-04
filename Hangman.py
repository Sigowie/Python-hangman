import time #Import time module

name = input("What is your name?") #setter navn"

print "Hello, " + name, "Time to play some hangman!"

time.sleep(1) #Vent et sekund#

print "Start guessing..."

time.sleep(0.5)

word = "secret" #Sett ord

guesses = '' #Setter tom variabel

turns = 10

while turns > 0: 
    failed = 0

    for char in word:

        if char in guesses:

            print char,

        else:

            print "_",

            failed +=1

        if failed == 0:
            print "You won"


            break

    guess = input ("guess a character:")

    guesses     += guess

    if guess not in word:

        turns -= 1

        print "You have", + turns, "more guesses"

        if turns == 0:

            print "you lose"
    


