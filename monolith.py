from enum import Enum
from random import shuffle

class Tabletop:

  def __init__(self):
    self.__firstPlayer = None
    self.__playerCount = 0
    self.__currPlayer = None
    self.__lastPlayer = None
    self.__pile = None

  def newGame(self):
    self.__pile = Pile()  
  
  def newPlayer(self):
    self.__playerCount += 1
    guy = Player(self.__playerCount)
  
    if self.__firstPlayer is None:
      self.__firstPlayer = guy and self.__lastPlayer = guy and self.__currPlayer = guy
    
    else:
      self.__firstPlayer = guy
    
      '''
      Set "guy" as next in Player linked list
      '''
    
      person = Player(self.__playerCount - 1)
      person.setNext()
      
  def isEmpty(self):
    if self.__firstPlayer is None and self.__lastPlayer is None:
      return True
    else:
      return False
    
  def __len__(self):
    curr = self.__firstPlayer
		count = 0
    if self.__firstPlayer is None:
      return count
		while curr != self.__lastPlayer:
			curr = curr.getNext()
			count+=1
		return count+1 
      
  def startDeal(self):
    if self.isEmpty() or len(Tabletop) < 2:
      print("Not Enough Players")
    else:
      player = self.__firstPlayer
      player.newHand(self.__pile)
      
      while player is not None:
        player.getNext()
        player.newHand(self.__pile)
        
    print("Hands Dealt")


class Player:

  def __init__(self, number):
    self.__playerNumber = number
    self.__score = 0
    self.__prev = number - 1
    self.__next = None
    self.__cards = []
  
  def setNext(self):
    self.__next = self.__playerNumber + 1
    
  def getNext(self):
    if self.__next is not None:
      return self.__next
    else:
      return
    
  def showCards(self):
    for i in self.__cards:
      print(str(i))
  
  def getScore(self):
    return self.__score

  def getNumber(self):
    return self.__playerNumber

  def newHand(self, varPile):
    for i in range(3):
      self.__cards.append(varPile.take())
      self.__score += self.__cards[-1].value

  def drawCard(self, varPile, throwIndex):
    self.__score -= self.__cards[throwIndex].value
    del self.__cards[throwIndex]
    self.__cards.append(varPile.take())
    self.__score += self.__cards[-1].value
    
  
  
class Pile:
    def __init__(self):
        self.__cards = [
            Card(value, suit) for value in CardValue for suit in CardSuit
        ]
        shuffle(self.__cards)
    
    def take(self):
      self.__cards.pop()
      
    def newPile(self):
      for i in self.__cards
        self.__cards.pop()
      
      self.__cards = [
            Card(value, suit) for value in CardValue for suit in CardSuit
        ]
        shuffle(self.__cards)
      
      

'''
Credits to Stephen Raunch 
'''

class CardValue(Enum):
    Ace = 1
    Deuce = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13


class CardSuit(Enum):
    Club = 1
    Heart = 2
    Diamond = 3
    Spade = 4


class Card(tuple):

    def __new__(cls, value, suit):
        assert isinstance(value, CardValue)
        assert isinstance(suit, CardSuit)
        return tuple.__new__(cls, (value, suit))

    @property
    def value(self):
        return self[0]

    @property
    def suit(self):
        return self[1]

    def __str__(self):
        return "{} of {}s".format(self.value.name, self.suit.name)

    def __setattr__(self, *ignored):
        raise NotImplementedError

    def __delattr__(self, *ignored):
        raise NotImplementedError
      
