#This program does a monte hall program for the game Cosmic Wimpout
#Usman Ghani
#11/1/17
#CS103 Lab 11

from random import *
from collections import *



def monte2():    

    #[This function checks the statistics for a certain number of Cosmic Wimpout turns and a certain number of rerolls.]
 

    numberOfRerolls = 20
    numberOfTurns = 100

    turnNumber = [0]

    pointTracker = []
    turnTracker = []
    rollTracker = []

    rollsToLose = []
    for i in range(numberOfTurns):
        rollNumber = [0]
        
        initialDice = [0,0,0,0,0]
        initialPoints = [0]
    
        play(initialDice, initialPoints, rollNumber, numberOfRerolls)
        turnNumber[0] += 1
        
        
        finalPoints = initialPoints[0]
        finalRolls = rollNumber[0]
        finalTurn = turnNumber[0]

        if finalPoints == 0:
            rollsToLose.append(finalRolls)

        pointTracker.append(finalPoints)
        turnTracker.append(finalTurn)
        rollTracker.append(finalRolls)

        del initialDice[:-1]

    print("\nDATA RESULTS")
    print("----------------------------------------")
  
        
   

    avgRollsToLose = sum(rollsToLose)/len(rollsToLose)
    avgPoints = sum(pointTracker)/ len(pointTracker)
    percentLost = (len(rollsToLose))/numberOfTurns * 100
    print("Number of turns: %d" % numberOfTurns)
    print("Max roll amount: %d" % numberOfRerolls)
    print("Number of losers: ", len(rollsToLose))
    print("Percent of losers: %d percent" % percentLost)
    print("Average amount of rolls to lose: %d" % avgRollsToLose)
    print("Average number of points: %d" % avgPoints)
    
      


         
def roll(thing):
    #[This function randomly rolls 6 dice]
    #params: thing (list)
    #output: randomizes the 6 element list of dice numbers

    for i in range(0,5):
        thing[i] = randint(1,6)
    
        



def results(thing):
    #[This function displays the results of the dice]
    #params: thing (list)
    #output: The value of each dice in the list
    #For simulation purpose, wildcard will always turn into a 5 to try to prevent turn from ending.

    for i in range (0,5):
        num = i + 1
        result = thing[i]
        print("\nDice #%d: [%d]" % (num, result))

    if thing[0] == 3:
        if (thing[0] == 3):
            print("You rolled a wild card. It will be turned into a 5")
            thing[0] = 5
            #print("\nYou rolled a wild card (3) on your Dice #1.")
            #choice = input("Would you like to change the value of your wildcard?(y/n): ")
            #if choice == "y" or choice == "yes":
             #   thing[0] = int(input("What would you like to change the value of your wildcard to?: "))
              #  while thing[0] < 1 or thing [0] > 6:
               #     print("Please enter a number between 1 and 6)")
                #    thing[0] = int(input("What would you like to change the value of your wildcard to: "))
           # else:
            #    print("\nDice #1 will remain at the value of 3")

def isOver(thing, tracker):
    #[This function checks for a freight train of 1 or 5 to end game]
    #params: thing (list)
    #output: Victory or Loss message and ending of program

    if (thing == [1, 1, 1, 1, 1]):
        print("\nSorry you lose.")
        tracker[0] = 0
        thing.append(0)
    elif(thing == [6, 6, 6, 6, 6]):
        print("\nCongratulations, you win!")
        tracker[0] = 9999
        thing.append(0)

def isFreight(thing, tracker, r, maxR):
    #[This function checks for a freight train of 2, 4, or 5]
    #params: thing (list), tracker (list)
    #returns:

    for i in [2, 4, 5]:
        
        if (thing == [i,i,i,i,i]):
            score = i * 100
            tracker[0] = tracker[0] + score
            totalScore = tracker[0]
            print("\nYou got %d points on this roll. You have %d total points. Time to roll again..." % (score, totalScore))
            play(thing, tracker, r, maxR)

def isFlash(thing, tracker, r, maxR):
    #[This function checks for a flash]
    #params: thing (list), tracker (list)
    #returns:

    def newRoll(b):
        print("\nYou have one unscoring die in this roll. You must roll it again.")
        a = randint(1,6)

        while a == b:
            print("You have rolled", flash)
            print("\nYou have one unscoring die in this roll, you must roll it again")
            a = randint(1,6)
        if a == 5:
            print("You have rolled a 5. You gain 5 points. Since you have scored with all 5 dice you must roll again!")
            tracker[0] += 5
            totalPoints = tracker[0]
            play(thing, tracker, r, maxR)
        elif a == 1:
            print("You have rolled a 1. You gain 10 points. Since you have scored with all 5 dice you must roll again!")
            tracker[0] += 10
            totalPoints = tracker[0]
            play(thing, tracker, r, maxR)
        else:
            print("You rolled a %d." % a)
            print("Your rerolls did not garner any points.")
            totalPoints = tracker[0]
            print("Your total score is: %d" % totalPoints)
            rollAgain = "no"
            goAgain = "yes"
            if r[0] < maxR:
                play(thing, tracker, r, maxR)
            else:
                thing.append(0)            
 
        

    c = Counter(thing)
    numberOf = []
    for x in range(1,7):
        value = int(c[x])
        numberOf.append(value)

    for i in range(0,6):
        if numberOf[i] == 3:
            flash = i + 1
            score = (i +1) * 10
            tracker[0] += score
            totalScore = tracker[0]
            print("\nYou scored a flash with three %d 's. You gain %d points. Your total score is now %d." % (flash, score, totalScore))
            if numberOf[0] == 2:
                tracker[0] += 20
                totalScore = tracker[0]
                print("You got two 1's in addition to your flash. You gain 20 points!")
                print("You scored with all dice you must continue to roll")
                print("Your total score is: %d" % totalScore)
                play(thing, tracker, r, maxR)
            elif numberOf[4] == 2:
                tracker[0] += 10
                totalScore = tracker[0]
                print("You got two 5's in addition to your flash. You gain 10 points!")
                print("You scored with all dice you must continue to roll")
                print("Your total score is: %d" % totalScore)

            elif numberOf[4] == 1 and numberOf[0] == 1:
                tracker[0] += 15
                totalScore = tracker[0]
                print("You gota 1 and a 5 in addition to your flash. You gain 15 points!")
                print("You scored with all dice you must continue to roll")
                print("Your total score is: %d" % totalScore)

            elif numberOf[0] == 1: 
                tracker[0] += 10
                totalScore = tracker[0]
                print("\nYou have rolled a 1 in addition to your flash")
                print("You gain an additional 10 points")
                newRoll(flash)

            elif numberOf[4] == 1:
                tracker[0] += 5
                totalScore = tracker[0]
                print("\nYou have rolled a 5 in addition to your flash")
                print("You gain an additional 5 points")
                newRoll(flash)

            else:
                print("\nYou have two unscoring dice in this roll")
                print("Time to reroll both of these dice...")
                rollAgain = "yes"
                while rollAgain == "yes":
                    reroll = [0,0]
                    for i in range(0,2):
                        reroll[i] = randint(1,6)
                    if  flash not in reroll and 1 not in reroll and 5 not in reroll:
                        print("You rolled ", reroll[0], "and ", reroll[1])
                        print("\nYour rerolls did not garner any points.")
                        print("Your total score is: " + str(tracker[0]))
                        rollAgain = "no"
                        goAgain = "yes"
                        if r[0] < maxR:
                            play(thing, tracker, r, maxR)
                        else:
                            thing.append(0)
                    elif reroll == [1,5] or reroll == [5,1]:
                        print("You rolled a 5 and a 1")
                        tracker[0] += 15
                        totalScore = tracker[0]
                        print("You gain 15 points. Since you scored with all 5 dice you must roll again!")
                        rollAgain = "no"
                        play(thing, tracker, r, maxR)
                    elif reroll == [5,5]:
                        print("You rolled a 5 and a 5")
                        tracker[0] += 10
                        totalPoints = tracker[0]
                        print("You gain 10 points .Since you scored with all 5 dice you must roll again!")
                        rollAgain = "no"
                        play(thing, tracker, r, maxR)
                    elif reroll == [1,1]:
                        print("You rolled a 1 and a 1")
                        tracker[0] += 20
                        totalPoints = tracker[0]
                        print("You gain 20 points .Since you scored with all 5 dice you must roll again!")
                        rollAgain = "no"
                        play(thing, tracker, r, maxR)
                    elif reroll == [flash,flash]:
                        print("You rolled", flash, "and", flash)
                    elif (reroll[0] == flash or reroll[1] == flash) and reroll != [flash,flash]:
                        print("You rolled " + str(reroll[0]) + " and " + str(reroll[1]))
                        newRoll(flash)
                        rollAgain = "no"
                    elif 1 in reroll:
                        print("You rolled ", reroll[0], "and ", reroll[1])
                        tracker[0] += 10
                        totalPoints = tracker[0]
                        print("You gain 10 points.")
                        newRoll(flash)
                        rollAgain = "no"
                    elif 5 in reroll:
                        print("You rolled ", reroll[0], "and ", reroll[1])
                        tracker[0] += 5
                        totalPoints = tracker[0]
                        print("You gain 5 points.")
                        newRoll(flash)
                        rollAgain = "no"

def isFlash4(thing, tracker, r, maxR):
    #[This function checks for a flash of 4]
    #params: thing (list), tracker (list)
    #returns:

    def newRoll(b):
        print("\nYou have one unscoring die in this roll. You must roll it again.")
        a = randint(1,6)

        while a == b:
            print("You have rolled", flash)
            print("\nYou have one unscoring die in this roll, you must roll it again")
            a = randint(1,6)
        if a == 5:
            print("You have rolled a 5. You gain 5 points. Since you have scored with all 5 dice you must roll again!")
            tracker[0] += 5
            totalPoints = tracker[0]
            play(thing, tracker, r, maxR)
        elif a == 1:
            print("You have rolled a 1. You gain 10 points. Since you have scored with all 5 dice you must roll again!")
            tracker[0] += 10
            totalPoints = tracker[0]
            play(thing, tracker, r, maxR)
        else:
            print("You rolled a %d." % a)
            print("Your rerolls did not garner any points.")
            totalPoints = tracker[0]
            print("Your total score is: %d" % totalPoints)
            rollAgain = "no"
            goAgain = "yes"
            if r[0] < maxR:
                play(thing, tracker, r, maxR)
            else:
                thing.append(0)
        

    c = Counter(thing)
    numberOf = []
    for x in range(1,7):
        value = int(c[x])
        numberOf.append(value)

    for i in range(0,6):
        if numberOf[i] == 4:
            flash = i + 1
            score = (i +1) * 10
            tracker[0] += score
            totalScore = tracker[0]
            print("\nYou scored a flash with four %d 's. You gain %d points. Your total score is now %d." % (flash, score, totalScore))
            newRoll(flash)
    
                        
                        


def plainPoints(thing, tracker, r, maxR):
    #[This function checks for points if there is not a flash or a freight]
    #param: thing (list), tracker (list)
    #returns:

    c = Counter(thing)
    numberOf = []
    for x in range(1,7):
        value = int(c[x])
        numberOf.append(value)
    keepGoing = True
    for x in range(0,6):
        if numberOf[x] >= 3:
            keepGoing = False
        

    
    if keepGoing == True:
        print("You have not gotten a flash or a freight with this roll.")
        if 5 not in thing and 1 not in thing:
            print("You did not score any points on this roll! You wimpout you noob! 0 points for this round.")
            tracker[0] = 0
            totalPoints = tracker[0]
            thing.append(0)
            keepGoing = False
        else:
            fives = numberOf[4]
            ones = numberOf[0]
            print("\nNumber of fives: %d. Number of ones: %d." % (fives, ones))
            add = (fives * 5) + (ones * 10)
            tracker[0] = tracker[0] + add
            totalScore = tracker[0]
            print("You gain %d points. Your total score is: %d." % (add, totalScore))
            goAgain = "yes"
            if r[0] < maxR:
                play(thing, tracker, r, maxR)
            else:
                thing.append(0)
            keepGoing = False
        

    
                    
def play(dice, points, rNum, maxRolls):
    rNum[0] += 1
    while (len(dice) <= 5):
        ready = "r"
        while ready != "r":
             ready = input("\nPress 'r' to roll the dice!: ")
        roll(dice)
        results(dice)
        isOver(dice, points)
        isFreight(dice, points, rNum, maxRolls)
        isFlash(dice, points, rNum, maxRolls)
        isFlash4(dice, points, rNum, maxRolls)
        plainPoints(dice, points, rNum, maxRolls)
    
       
    
        

    

    
                    
                        
                        
                    
                
                
                
                
                
                
            
                

    
        
        
        
        
        
    


