class Tabletop:

  def __init__(self):
    self.__firstPlayer = None
    self.__playerCount = 0
    self.__currPlayer = None
    self.__lastPlayer = None

  def newGame(self):
    pass  
  
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
    
  def startDeal(self):
    pass


class Player:

  def __init__(self, number):
    self.__playerNumber = number
    self.__score = 0
    self.__prev = number - 1
    self.__next = None
  
  def setNext(self):
    self.__next = self.__playerNumber + 1
  
  def getScore(self):
    return self.__score

  def getNumber(self):
    return self.__playerNumber

  def newHand(self, varPile):
    pass

  def drawCard(self, varPile):
    pass

class Pile:
  
  def __init__(self):
    pass
