# External module import
import pydealer

# initialise a deck of cards 
deck = pydealer.Deck()

# initialise a second deck of cards called a "hand"
hand = pydealer.Stack()

# shuffle the deck
deck.shuffle()

# randomly select 4 cards from the intial deck 
dealt_cards = deck.deal(4)

# print the initial deck
print(dealt_cards)

memory = input("Memorise a Card from the given options and i will make it disappear!\nPress the enter key when you are ready! ")

# second deck of card uses 3 cards from the initial deck 
hand.add(dealt_cards[0:3])
 
# adds one random card to the new deck
hand.add(deck.deal(1))

# shuffle the second deck 
hand.shuffle()

# print the second deck 
print(hand)


mindFreak = input("Did I manage to remove the card you were thinking of?(y or n): ")


if mindFreak == "y":
  print("I am the best Mind-Reader!!!")
else:
  print("I will try again :(")
