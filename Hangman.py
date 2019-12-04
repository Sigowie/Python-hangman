import time #Import time module
import random #import random module

name = raw_input("What is your name?") #setter navn

print "Hello, " + name, "Time to play some hangman!"

time.sleep(1) #Vent et sekund

print "Start guessing..."

time.sleep(0.5)

lines = open("words.txt").readlines() #åpner txt dokument
line = lines[0] #settning fra txt doukument

words = line.split() #spliter inn i liste baser på åpenrom

word = random.choice(words) #Sett ord

guesses = '' #Setter tom variabel

turns = 10

while turns > 0:#sett while loop
    failed = 0

    for char in word: #for loop for alle karakterer i ord
        
        if char in guesses: #ser om karakteren er i spillers gjetting

            print char,

        else:

            print "_",

            failed +=1

    if failed == 0:
        print "You won"

        break

    guess = raw_input ("guess a character:")

    guesses += guess

    if guess not in word:

        turns -= 1

        print "You have", + turns, "more guesses"

        if turns == 0:

            print "you lose"
    


