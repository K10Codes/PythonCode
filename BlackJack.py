#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
suits = ('Hearts','Diamond','Spade','Clubs')
ranks = ('Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King')
values = {'Ace':1,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10}

class Card :
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + " of "+self.suit


class Deck : 
    def __init__(self):
        self.deck = []
        for suit in suits :
            for rank in ranks:
                self.deck.append(Card(suit,rank))
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()
    
    def deckSize(self):
        return len(self.deck)

    
class Player :
    def __init__(self,score,chips=0):
        self.chips = chips
        self.score = score 
        
    def bet(self,chips):
        self.chips = self.chips-chips
    
    def addScore(self,score):
        self.score = self.score+score 
        

def getPlayerScore(cards):
    score = 0
    for card in cards:
        score = score + values.get(card.rank)
    
    return score

def dealCard(deck):
    
    card = deck.deal()
    print('Card drawn is {}'.format(card))
    return card

def dealPlayerCards(deck):
    
    pCard1 = dealCard(deck)
    pCard2 = dealCard(deck)
    pScore = getPlayerScore([pCard1,pCard2])
    player = Player(pScore,10)
    return player

def checkIfBusted(score):
    if(score>21):
        return True
    else:
        return False
    
def initDeck():
    deck = Deck()
    deck.shuffle()
    return deck

def letsPlay():
    print()
    print('*** LETS BEGIN ***')
    dealerCardShown = False
    print('Shuffling deck!')
    deck = initDeck()
    
    print('Drawing player\'\s cards!')
    player = dealPlayerCards(deck)
    
    
    print('Drawing dealer\'\s cards!')
    dCard1 = dealCard(deck)
    dCard2 = deck.deal()
    
    pScore = getPlayerScore([dCard1])
    dealer = Player(score=pScore)
   
    playDealer = False
    keepPlaying = True 

    print('Dealer\'\s score is {}'.format(dealer.score))

    while keepPlaying :
        pChoice = input('Your score is {}. Hit or stay?(Enter H or S)'.format(player.score))
        if(pChoice == 'H'):
            if(player.chips == 0):
                print('You are out of chips!')
                playDealer = True
            else:
                pCard = dealCard(deck)
                player.addScore(getPlayerScore([pCard]))
                print('Your score is {}'.format(player.score))

                if(checkIfBusted(player.score)) :
                    keepPlaying = False
                    print('Player busted.Dealer wins!')
                
                elif player.score == 21:
                    keepPlaying = False
                    print('Player wins!')
                    
        else:
            print('Your score is {}'.format(player.score))
            playDealer = True
            keepPlaying = False

    while playDealer :
        if(not dealerCardShown):
            print('Showing dealer\'\s second card.{}'.format(dCard2))
            dealer.addScore(getPlayerScore([dCard2]))
            dealerCardShown = True
            
        else:
            print('Dealer draws card!')
            dCard = dealCard(deck)
            dealer.addScore(getPlayerScore([dCard]))
            
        print('Dealer\'\s score is {}'.format(dealer.score))

        if(dealer.score>21):
            print('Dealer busted.Player wins!')
            playDealer = False

        elif(dealer.score > player.score):
            print('Dealer wins!')
            playDealer = False
    
    rematch = input('Rematch(Y/N)?')
    if(rematch == 'Y'):
        letsPlay()
    else :
        print('Thanks for playing!')

letsPlay()


# In[ ]:





# In[ ]:




