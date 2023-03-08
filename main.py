# importing the random number generator function
import random
import sys
if len(sys.argv) > 1:
  random.seed(int(sys.argv[1]))
# initializing my variables for scores
score1 = 0
score2 = 0
# initializing variables to start the while loops
choice1 = "y"
choice2 = "y"
i = 0
# Start of the game 
print("Welcome to Go Big or Go Small")
while i <= 75:
    print("++++++++++BEGIN ROUND++++++++++")
    print("Player 1's turn")
    choice3 = " "
    choice4 = " "
    count3 = 0
    count4 = 0
    double = 0
    double1 = 0
    choose = " "
    choose1 = " "
    while double != range(1,7):
        # player one chooses what double numbers they don't want
        double = int(input("What number do you want to avoid rolling doubles of?"))
        if double >=1 and double <=6:
            break
        else:
            continue        
    while choose != "l" or choose != "s": 
        # player one chooses whether they want to use the bigger dice or smaller dice for score
        choose = input("Do you want to use the smaller or larger of the dice (s or l)?")
        if choose == "l":
            break
        elif choose == "s":
            break
        else: 
            continue
    while choice1 == "y":
        count1 = 0
        # Using a random number generator for the dice
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        # scoring the dice from the players decision
        if choose == "l":
            #**** this is a for rolling doubles ****
            if die1 == double and die2 == double:
                print("You roll a", die1, "and", die2)
                count3 = 0
                break
            elif die1 >= die2:
                count1 = die1
            elif die2 >= die1:
                count1 = die2            
        elif choose == "s":
            #**** this is a for rolling doubles ****
            if die1 == double and die2 == double:
                print("You roll a", die1, "and", die2)
                count3 = 0
                break
            elif die1 >= die2:
                count1 = die2
            elif die2 >= die1:
                count1 = die1    
        # used 2 different variables for each player one for a score for that single roll and the other for the overall score for the game
        # if the player score more than 15pts for the round, their turn is over
        count3 += count1
        print("You roll a", die1, "and", die2)
        print("Your score for this roll is", count1)
        if count3 > 15:
            count3 = 0
            print("Your current total for this round is", count3)
            break
        print("Your current total for this round is", count3)
        # choice to roll again and continue the while loop or to end the turn
        while choice3 == " ":
            choice1 = input("Do you want to roll again (y or n)?")
            if choice1 == "n":
              break
            elif choice1 == "y":
              break
            else:
              continue
    print("Your turn is over -- you scored", count3, "points for this round")
    score1 += count3
    print("Player 2's turn")
    choice1 = "y"
    while double1 != range(0,7):
        # player one chooses what double numbers they don't want
        double1 = int(input("What number do you want to avoid rolling doubles of?"))
        if double1 >=1 and double1 <= 6:
            break
        else:
            continue
    while choose1 != "y" or choose1 != "n":
        # player 2 gets to choose if they want to count only the large dice or the small dice for points
        choose1 = input("Do you want to use the smaller or larger of the dice (s or l)?")
        if choose1 == "l":
            break
        elif choose1 == "s":
            break
        else:
            continue
    # used a while loop for the roll again and continue the 2nd players turn
    while choice2 == "y":
        count2 = 0
        # using the random number generator for dice 1 and dice 2
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print("You roll a", die1, "and", die2)
        # scoring the dice according to the players decision
        if choose1 == "l":
            #**** this is a for rolling doubles *****
            if die1 == double1 and die2 == double1:
                print("You roll a", die1, "and", die2)
                count2 = 0 
                break
            elif die1 >= die2: 
                count2 = die1
            elif die2 >= die1:
                count2 = die2
        elif choose1 == "s":
            #**** this is a for rolling doubles ****
            if die1 == double1 and die2 == double1:
                print("You roll a", die1, "and", die2)
                count2 = 0
                break
            elif die1 >= die2:
                count2 = die2
            elif die2 >= die1:
                count2 = die1
            
        # used 2 different variable for player 2 as well to have a score for the roll and the overall game score
        # to limit the amount of points the player can gain per a turn to 15
        count4 = count4 + count2
        
        print("Your score for this roll is", count2)
        if count4 > 15:
            print("Your current total for this round is", count4)
            count4 = 0
            break
        print("Your current total for this round is", count4)
        # player gets to choose to continue the loop and roll again or end their turn
        while choice4 == " ":
            choice2 = input("Do you want to roll again (y or n)?")
            if choice2 == "n":
              break
            elif choice2 == "y":
              break
            else:
              continue
    print("Your turn is over -- you scored", count4, "points for this round")
    score2 += count4
    choice2 = "y"
    # this is the end of round one and printing out the scores for the game so far
    print("--Here is the updated score for the game--")
    print("Player 1 has", score1, "points total")
    print("Player 2 has", score2, "points total")
    # Continuing to the next round until a player reaches 75 points
    if score1 > score2:
        i == score1
        if score1 >= 75: 
          break
    elif score1 < score2:
        i == score2
        if score2 >= 75:
           break 
# final scoring & determining the winner
if score1 > score2:
    print("Player 1 wins!")
elif score2 > score1:
    print("Player 2 wins!")
elif score1 == score2:
    print("It is a tie!")
enter = input("Hit enter to end.")