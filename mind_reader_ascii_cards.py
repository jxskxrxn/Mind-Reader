# External module import
import pydealer
import keyboard
import random
from colored import fg

def ascii_hand(hand):
    """
        Function that converts pydealer cards into
        an ascii image of the card.
    :param hand: An array of pydealer() cards.
    :return: An ascii representation of a card
    """

    # Instantiating variables
    ascii_hand = ""

    # Defining suits ascii code
    hearts = "\u2665"
    diamonds = "\u25C6"
    spades = "\u2660" # Duplication of symbol that why you were getting 'duplicate' card
    clubs = "\u2663"

    # Iterates through array and assigns card_print and suit a value
    for card in hand:
        if card.value in ("King", "Queen", "Jack", "Ace"):
            rank = card.value[0]
        else:
            rank = card.value
        if card.suit == "Hearts":
            card_suit = hearts
        elif card.suit == "Diamonds":
            card_suit = diamonds
        elif card.suit == "Spades":
            card_suit = spades
        else:
            card_suit = clubs

        # Rjust method returns a right-justified string, chose the max width and
        # the character to fill the remaining space
        card_print = f"|{str(rank).rjust(2,' ')}  {card_suit}|"

        # Adds the new card to the ascii hand
        ascii_hand += card_print
    print(" ______" * (len(hand)))
    print(ascii_hand)
    print("|     |" * (len(hand)))
    print("|_____|" * (len(hand)))

# initialise a deck of cards
deck = pydealer.Deck()

# initialise a second deck of cards called a "hand"
hand = pydealer.Stack()

# shuffle the deck
deck.shuffle()

# randomly select 4 cards from the initial deck
dealt_cards = deck.deal(4)

# print the initial deck
ascii_hand(dealt_cards)

memory = input(
    "Memorise a Card from the given options and i will make it disappear!\nPress the enter key when you are ready! ")


# second deck of card uses 3 random cards from the initial deck
pick_cards = random.sample(range(4), 3)
for p_cards in pick_cards:
    hand.add(dealt_cards[p_cards])

# adds one random card to the new deck
hand.add(deck.deal(1))

# shuffle the second deck
hand.shuffle()

# print the second deck
ascii_hand(hand)

print("Did I manage to remove the card you were thinking of?(y or n): ")

# Keyboard Listener checks if the key Y or R are pressed
while True:
    if keyboard.is_pressed('y') or keyboard.is_pressed('Y'):
        print(fg("green") + "I am the best Mind-Reader!!!")
        break
    elif keyboard.is_pressed('n') or keyboard.is_pressed('N'):
        print(fg("red") + "I will try again :(")
        break
