fourdigit = []
import random

#instructions
print ("Guess a four digit number. You will be notified if each digit is either correct or incorrect. Then, you will be notified how many digits are correct but in the wrong spot. You will have 4 chances to guess.")
for i in range (0,4):
    randigit = random.randint (0,9)
    fourdigit.append (randigit)


str(fourdigit)

# guessing the number
for i in range (0,4):
    userinput1 = input("what is your guess: ")

    # separating each digit in the guess
    str(userinput1)
    guess = list(userinput1)

    if (guess[:0]) in (fourdigit[:0]):
        print ("yes the first digit is correct")
    else: print("the first digit is wrong")

    if (guess[:1]) in (fourdigit[:1]):
        print ("yes the second digit is correct")
    else: print("the second digit is wrong")

    if (guess[:2]) in (fourdigit[:2]):
        print ("yes the third digit is correct")
    else: print("the third digit is wrong")

    if (guess[:3]) in (fourdigit[:3]):
        print ("yes the fourth digit is correct")
    else: print("the fourth digit is wrong")


    #     how many are correct but in wrong spot
    numright = 0

    if (guess[:1]) in (fourdigit):
        numright.add (1)
    if (guess[:2]) in (fourdigit):
        numright.add (1)
    if (guess[:3]) in (fourdigit):
        numright.add (1)
    if (guess[:4]) in (fourdigit):
        numright.add (1)

    print ("You guessed" + (numright) + "digits correct but they're in the wrong spot")



print ("Thanks for playing. The Correct number was:" + (fourdigit))



    # indivdigit = 0
    #set indivdigit var to the first digit (inndex 0) from userinput
    #check if indivdig is in four digit
    #output
    #change indivdig to index 1






    #looping through to check if each digit is in fourdigit
     # for i in range (0,4):
     #     if fourdigit in userinput1:
     #         print("correct")
     #     else:
     #         print ("all digits were wrong")












