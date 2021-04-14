import random

names = ["1","2","3","4","5","6","7","8","9","10","J","Q","K"]
suits = ["Spades","Hearts","Clubs","Diamonds"]


def createADeck():
  deck = []
  for s in suits:
    for v in names:
      deck.append((v,"of",s))
  return deck
  
deck = createADeck()

random.shuffle(deck)

print(random.sample(deck, 4))

memory = input("Memorise a Card from the given options and i will make it disappear! \nPress the enter key when you are ready! ")

print(random.sample(deck, 4))

mindFreak = input("Did I manage to remove the card you were thinking of?: ")

print("I am the best mind reader!! Mind = Blown!!")


