<img src="OOP_Unit05_Inheritance_Ex18.1.jpg?raw=true"> 

---

```python
# Exercise 18.2
"""Write a Deck method called deal_hands that takes two parameters, the number of hands and the number of cards per hand.
It should create the appropriate number of Hand objects, deal the appropriate number of cards per hand, and return a list of Hands."""

import random

class Card:
    """
    Represents a single playing card with a suit and a value.
    """
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, suit, value):
        """
        Initializes a card with a given suit and value.
        :param suit: The suit of the card (Hearts, Diamonds, Clubs, Spades).
        :param value: The value of the card (2-10, Jack, Queen, King, Ace).
        """
        self.suit = suit
        self.value = value

    def __repr__(self):
        """
        Returns a string representation of the card.
        :return: A string in the format 'value of suit'.
        """
        return f"{self.value} of {self.suit}"

class Deck:
    """
    Represents a deck of 52 playing cards.
    """
    def __init__(self):
        """
        Initializes a deck by creating 52 cards and shuffling them.
        """
        self.cards = [Card(suit, value) for suit in Card.suits for value in Card.values]
        random.shuffle(self.cards)

    def deal_card(self):
        """
        Deals a single card from the deck.
        :return: The dealt card or None if the deck is empty.
        """
        return self.cards.pop() if self.cards else None

    def deal_hands(self, num_hands, cards_per_hand):
        """
        Deals a specified number of hands with a specified number of cards per hand.
        :param num_hands: The number of hands to deal.
        :param cards_per_hand: The number of cards per hand.
        :return: A list of Hand objects.
        """
        # Create the specified number of Hand objects
        hands = [Hand() for _ in range(num_hands)]
        
        # Deal the specified number of cards to each hand
        for _ in range(cards_per_hand):
            for hand in hands:
                hand.add_card(self.deal_card())
        
        return hands

class Hand:
    """
    Represents a hand of playing cards.
    """
    def __init__(self):
        """
        Initializes an empty hand.
        """
        self.cards = []

    def add_card(self, card):
        """
        Adds a card to the hand.
        :param card: The card to add.
        """
        if card is not None:
            self.cards.append(card)

    def __repr__(self):
        """
        Returns a string representation of the hand.
        :return: A string in the format 'Hand([list of cards])'.
        """
        return f"Hand({self.cards})"

# Usage example
if __name__ == "__main__":
    # Create a deck of cards
    deck = Deck()
    
    # Deal 4 hands with 5 cards each
    hands = deck.deal_hands(4, 5)
    
    # Print each hand
    for i, hand in enumerate(hands):
        print(f"Hand {i + 1}: {hand}")

```

```python
# Exercise 18.2 Output

<class '__main__.Deck'>
9 of Clubs
Jack of Clubs
Jack of Hearts
2 of Spades
Queen of Spades



```

---

[Return to Module 2 Unit 5](OOP_Unit05.md)
