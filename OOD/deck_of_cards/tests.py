from cards import *
from random import seed

seed(0)
def print_hand(h):
        print(f"Hand {len(h)}: ", end="")
        for c in h:
                print(c, end=" ")
        print()

def test_deck():
        d = Deck()
        d.print()
def test_deck_shuffle():
        d = Deck()
        d.shuffle()
        d.print()
def test_hand():
        num = 5
        d = Deck()
        d.shuffle()
        h = d.deal(num)
        print_hand(h)
        assert num == d.dealt

def test_deal():
        num = 5
        d = Deck()
        d.shuffle()
        d.print()
        h = d.deal(num)
        h += d.deal(num)
        # print_hand(h)
        d.print()
        assert num*2 == d.dealt

def test_hand_points_for_BJ():
        num = 2
        d = BlackJackDeck()
        d.shuffle()
        h = d.deal(num)
        print_hand(h)
        p_h, p_s = 0, 0
        for c in h:
                p_h += c.hard()
                p_s += c.soft()
        print(f"Hard points:{p_h}, soft points:{p_s}")

test_hand_points_for_BJ()
		