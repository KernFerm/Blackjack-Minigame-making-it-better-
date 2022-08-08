import random
import time

print('Welcome to Blackjack')

#Cards avaliable to be selected
cards = [1,2,3,4,5,6,7,8,9,10]

#Preselecting the cards for each player
playerCardOne = random.choice(cards)
playerCardTwo = random.choice(cards)
playerCardThree = random.choice(cards)
playerCardFour = random.choice(cards)
playerCardFive = random.choice(cards)

dealerCardOne = random.choice(cards)
dealerCardTwo = random.choice(cards)

#Displaying the cards and asking the player if they want to hit stand or forfeit
print('These are the Dealers cards',dealerCardOne,'X')
time.sleep(2)
print('These are your cards',playerCardOne,playerCardTwo)
time.sleep(2)
print('Hit, Stand, Forfeit')
time.sleep(2)

playerInput = input()

if playerInput == 'hit':
    print('Your cards are now',playerCardOne,playerCardTwo,playerCardThree)
    time.sleep(2)

if playerInput == 'stand':
    print("The Dealer's cards are",dealerCardOne,dealerCardTwo)
    time.sleep(2)
    print('Your cards are',playerCardOne,playerCardTwo)
    time.sleep(2)
    if playerCardOne + playerCardTwo >= dealerCardOne + dealerCardTwo:
        print("You Have Won Congrats!")
        quit()
    elif playerCardOne + playerCardTwo <= dealerCardOne + dealerCardTwo:
        print("You Have Lost HA")
        quit()

if playerInput == 'forfeit':
    print("Dealer's cards are",dealerCardOne,dealerCardTwo)
    time.sleep(2)
    print("Your cards are",playerCardOne,playerCardTwo)
    time.sleep(2)
    print('Your forfeited the dealer automaticly wins')
    time.sleep(2)
    quit()

if playerCardOne + playerCardTwo + playerCardThree >= 21:
    print("You've gone above 21 you busted")
    time.sleep(2)
    quit()

print('Hit, Stand, Forfeit')
time.sleep(2)

playerInputTwo = input()

if playerInputTwo == 'hit':
    print('Your cards are now',playerCardOne,playerCardTwo,playerCardThree,playerCardFour)
    time.sleep(2)

if playerInputTwo == 'stand':
    print("The Dealer's cards are",dealerCardOne,dealerCardTwo,)
    time.sleep(2)
    print('Your cards are',playerCardOne,playerCardTwo,playerCardThree)
    time.sleep(2)
    if playerCardOne + playerCardTwo + playerCardThree >= dealerCardOne + dealerCardTwo:
        print("You Have Won Congrats!")
        quit()
    elif playerCardOne + playerCardTwo + playerCardThree <= dealerCardOne + dealerCardTwo:
        print("You Have Lost HA")
        quit()

if playerInputTwo == 'forfeit':
    print("Dealer's cards are",dealerCardOne,dealerCardTwo)
    time.sleep(2)
    print("Your cards are",playerCardOne,playerCardTwo,playerCardThree)
    time.sleep(2)
    print('Your forfeited the dealer automaticly wins')
    time.sleep(2)
    quit()

if playerCardOne + playerCardTwo + playerCardThree + playerCardFour >= 21:
    print("You've gone above 21 you busted")
    time.sleep(2)
    quit()

print('Hit, Stand, Forfeit')
time.sleep(2)

playerInputThree = input()

if playerInputTwo == 'hit':
    print('Your cards are now',playerCardOne,playerCardTwo,playerCardThree,playerCardFour,playerCardFive)
    time.sleep(2)

if playerInputTwo == 'stand':
    print("The Dealer's cards are",dealerCardOne,dealerCardTwo,)
    time.sleep(2)
    print('Your cards are',playerCardOne,playerCardTwo,playerCardThree,playerCardFour)
    time.sleep(2)
    if playerCardOne + playerCardTwo + playerCardThree + playerCardFour >= dealerCardOne + dealerCardTwo:
        print("You Have Won Congrats!")
        quit()
    elif playerCardOne + playerCardTwo + playerCardThree + playerCardFour <= dealerCardOne + dealerCardTwo:
        print("You Have Lost HA")
        quit()

if playerInputTwo == 'forfeit':
    print("Dealer's cards are",dealerCardOne,dealerCardTwo)
    time.sleep(2)
    print("Your cards are",playerCardOne,playerCardTwo,playerCardThree,playerCardFour)
    time.sleep(2)
    print('Your forfeited the dealer automaticly wins')
    time.sleep(2)
    quit()

if playerCardOne + playerCardTwo + playerCardThree + playerCardFour + playerCardFive >= 21:
    print("You've gone above 21 you busted")
    time.sleep(2)
    quit()

print("Ok you 100% have a higher count then the dealer by now so you win!")