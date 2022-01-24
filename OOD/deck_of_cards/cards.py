from enum import Enum, unique
from typing import List
from random import shuffle as default_shuffle

# from abc import abstractmethod

@unique
class CardType(Enum):
	Hearts = '♥️'
	Diamonds = '♦️'
	Clubs = '♣️'
	Spades = '♠️'

@unique     
class Face(Enum):
        J = 11
        Q = 12
        K = 13

class Card:
        def __init__(self, _v, _t):
                self.card_type = _t             
                self.value = _v 
        def __str__(self):
                return self.card_type.value + " " + str(self.value)
class FaceCard(Card):
        def __init__(self, _v, _t):
                super().__init__(_v, _t)
                self.card_type = _t      
                if _v <= 13 and _v >= 11:       
                        self.value = Face(_v) 
                else:
                        raise ValueError("Value suplied is not a face value : ", str(_v))

        def __str__(self):
                return self.card_type.value + " " + self.value.name

class BlackJackCard(Card):
        def __init__(self, _v, _t):
                super().__init__(_v,_t)
        
        def hard(self):
                if self.value>1:
                        return self.value
                else: # A 
                        return 11
        def soft(self):
                if self.value>1:
                        return self.value
                else: # A 
                        return 1

class BlackJackFaceCard(FaceCard):
        def __init__(self, _v, _t):
                super().__init__( _v,_t)
        
        def hard(self):
                return 10
        def soft(self):
                return 10
class Deck:
        num_cards = 52
        card_range = range(1,14)
        dealt = 0
        cards:List[Card]
        def __init__(self, shuffle_method=default_shuffle):
                self.cards = [0]*self.num_cards
                for n,t in enumerate(CardType):
                        for i in self.card_range:
                                self.cards[ (n*len(self.card_range))+i-1] = FaceCard(i,t) if i>10 else Card(i,t)
                self.__shuffle_deck = shuffle_method
        def shuffle(self):
                self.__shuffle_deck(self.cards)
        
        def deal(self, num):
                hand = self.cards[self.dealt: self.dealt+num]
                self.dealt += num
                return hand

        def print(self):
                for i in range(self.dealt, self.num_cards):
                        # print(self.cards[i], end=" ,")
                        print(i, end=" ,")
                print()

class BlackJackDeck(Deck):
        num_cards = 52
        card_range = range(1,14)
        dealt = 0
        cards:List[Card]
        def __init__(self, shuffle_method=default_shuffle):
                super().__init__(default_shuffle)
                self.cards = [0]*self.num_cards
                for n,t in enumerate(CardType):
                        for i in self.card_range:
                                self.cards[ (n*len(self.card_range))+i-1] = BlackJackFaceCard(i,t) if i>10 else BlackJackCard(i,t)
                self.__shuffle_deck = shuffle_method
        def shuffle(self):
                self.__shuffle_deck(self.cards)
        
        def deal(self, num):
                hand = self.cards[self.dealt: self.dealt+num]
                self.dealt += num
                return hand

        def print(self):
                for i in range(self.dealt, self.num_cards):
                        # print(self.cards[i], end=" ,")
                        print(i, end=" ,")
                print()
