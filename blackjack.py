from typing import Self, List
# from itertools import product
import random


CARD_SYMBOLS = ["♠", "♥", "♦", "♣"]
                
CARD_VALUE_MAP = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "A": 11,
    "J": 12,
    "Q": 13,
    "K": 14
}

class Card:
    def __init__(self, number: str, symbol: str) -> None:
        if number not in CARD_VALUE_MAP:
            raise ValueError("Invalid card number.")
        if symbol not in CARD_SYMBOLS:
            raise ValueError("Invalid card symbol.")            
        self.__symbol = symbol
        self.__number = number

    @property
    def symbol(self):
        return self.__symbol
    
    @property
    def number(self):
        return self.__number 

    """ modificare metoda cmp sa se sorteze cartile din deck """

    def __str__(self) -> str:
        # trebuie sa returneze string
        return f"{self.__number} {self.__symbol}"

    def __repr__(self) -> str:
        return self.__str__()
    
    def get_value(self) -> int:
        return CARD_VALUE_MAP[self.__number]

    def __lt__(self, other):
    # __lt__ <
        return self.get_value() < other.get_number()

    def __le__(self, other):
    # __le__ <=
        return self.get_value() <= other.get_number()

    def __gt__(self, other):
    # __gt__ >
        return self.get_value() > other.get_number()
    
    def __ge__(self, other):
    # __ge__ >=
        return self.get_value() >= other.get_number()

    def __eq__(self, other):
        # operator overloading; return Boolean
        return self.get_value() == other.get_number() 

    def __add__(self, other: Self):
        # return int, dar un obiect nou
        return self.get_value() + other.get_value()
    
    def __radd__(self, other) -> int:
        return other + self.get_value()
    
    def __del__(self):
        """ Destructor """
        # print("Cartea a fost stearsa din memorie.")


class Deck:
    def __init__(self) -> None:
        # self.__deck = product(CARD_VALUE_MAP, CARD_SYMBOLS)
        self.__cards = []
        
        for symbol in CARD_SYMBOLS:
            for number in CARD_VALUE_MAP:
                self.__cards.append(Card(number, symbol))


    def __len__(self):
        # trebuie sa returneze int sau float
        return len(self.__cards)
    
    def get_cards(self, number) -> List[Card]:
        """ Return n cards. """
        if number > len(self.__cards):
            raise ValueError("Not enough cards in deck.")
        result = []
        for i in range(number):
            result.append(self.__cards.pop())
        return result

    def shuffle(self):
        """ Shuffles the deck. """
        random.shuffle(self.__cards)


d1 = Deck()
print(f"Number of cards in deck: {len(d1)}")
d1.shuffle()

x_cards = d1.get_cards(2)
for i in x_cards:
    print(f"{i.number}{i.symbol}")
print(f"Number of cards in deck: {len(d1)}")
print(sum(x_cards))




""" Jucatorul primeste 2 carti, verificam daca sunt egale cu 21 - loop. 
O sa avem o lista cu cartile primite de user, daca nu e 21, intrebam daca mai vrea carti. 
Daca vrea carti, ii mai dam o carte, suma tuturor, verificam daca e 21 etc. """