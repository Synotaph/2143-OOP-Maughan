# -*- coding: utf-8 -*-
import random
import os

class AsciiCard(object):

    suits = ['Spades','Hearts','Diamonds','Clubs']
    card_faces = []
    
    def __init__(self,cards_file):
        f = open(cards_file, 'r')
        count = 0
        card = ""
        
        for line in f:
            count += 1
            if line.strip() == "":
                continue
            card += line

            if count % 6 == 0:
                self.card_faces.append(card)
                card = ""

    def get_ascii(self,suit=None,rank=None):
        if suit == None or rank == None:
            return self.card_faces[0] ;
        s_index = self.suits.index(suit)
        return self.card_faces[((s_index * 13) + rank) - 1] ;

class Card(object):
    suits = ['Spades','Hearts','Diamonds','Clubs']
    ranks = [None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"]
    name_to_symbol = {
       'Spades':   '?',
       'Diamonds': '?',
       'Hearts':   '?',
       'Clubs':    '?',
    }

    def __init__(self, suit='', rank=0):
        #super().__init__('ascii_cards.txt')
        if type(suit) is int:
            self.suit = self.suits[suit]
        else:
            self.suit = suit
        self.rank = self.ranks[rank]
        self.value = rank
        self.symbol = self.name_to_symbol[self.suit]
        #self.card = self.get_ascii(self.suit,self.rank)

    def __str__(self):
        return "(%s, %s)" % (self.suit, self.rank)
           
    def __cmp__(self,other):
        t1 = self.name_to_symbol[self.suit],self.value
        t2 = self.name_to_symbol[other.suit],other.value
        return int(t1[1])<int(t2[1])
   
    def __lt__(self,other):
        return self.__cmp__(other)

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit,rank))

                
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return " ".join(res)
    
    def pop_card(self):
        return self.cards.pop()
        
    def shuffle(self):
        random.shuffle(self.cards)

class Hand(Deck):
    def __init__(self, size, deck):
        self.cards_in_hand = []
        self.newHand(size, deck)

    def __str__(self):
        res = []
        for card in self.cards_in_hand:
            res.append(str(card))
        return " ".join(res)
    
    def newHand(self, size, deck):
        deck.shuffle()
        if (len(self.cards_in_hand) == 0):
            self.fillHand(deck)
        else:
           self.cards_in_hand = []
           self.fillHand(deck)

    def fillHand(self, deck):
        for i in range(len(self.cards_in_hand), 5):
            self.cards_in_hand.append(deck.pop_card())

    def pullCard(self, pull, deck):
        del self.cards_in_hand[pull]
              
    def sortHand(self):
        self.cards_in_hand = sorted(self.cards_in_hand)

class video_poker(Hand):
    def __init__(self, score = 0):
        self.game_deck = Deck()
        self.game_deck.shuffle()
        self.game_hand = Hand(5, self.game_deck)
        self.score = score
        
    def find_score(self, hand):
        self.game_hand.sortHand()
        score = 0
        if (hand.cards_in_hand[1].value == (hand.cards_in_hand[0].value + 1) and hand.cards_in_hand[2].value == (hand.cards_in_hand[0].value + 2) and hand.cards_in_hand[3].value == (hand.cards_in_hand[0].value + 3) and hand.cards_in_hand[4].value == (hand.cards_in_hand[0].value + 4)):
            if (hand.cards_in_hand[0].suit == hand.cards_in_hand[1].suit and hand.cards_in_hand[0].suit == hand.cards_in_hand[2].suit and hand.cards_in_hand[0].suit == hand.cards_in_hand[3].suit and hand.cards_in_hand[0].suit == hand.cards_in_hand[4].suit):
                if (hand.cards_in_hand[0].value == 10):
                    score = 800
                else:
                    score = 50
            else:
                score = 4
        elif (hand.cards_in_hand[0].value == hand.cards_in_hand[1].value and hand.cards_in_hand[0].value == hand.cards_in_hand[2].value and hand.cards_in_hand[0].value == hand.cards_in_hand[3].value) or (hand.cards_in_hand[1].value == hand.cards_in_hand[2].value and hand.cards_in_hand[1].value == hand.cards_in_hand[3].value and hand.cards_in_hand[1].value == hand.cards_in_hand[4].value):
            if ((hand.cards_in_hand[0].value == 14 and hand.cards_in_hand[1].value == 14) or (hand.cards_in_hand[1].value == 14 and hand.cards_in_hand[2].value == 14)) or ((hand.cards_in_hand[0].value == 8 and hand.cards_in_hand[1].value == 8) or (hand.cards_in_hand[1].value == 8 and hand.cards_in_hand[2].value == 8)):
                score = 80
            elif (hand.cards_in_hand[0].value == 7 and hand.cards_in_hand[1].value == 7) or (hand.cards_in_hand[1].value == 7 and hand.cards_in_hand[2].value == 7):
                score = 50
            else:
                score = 25
        elif (hand.cards_in_hand[0].value == hand.cards_in_hand[1].value and hand.cards_in_hand[0].value == hand.cards_in_hand[2].value):
            if hand.cards_in_hand[3].value == hand.cards_in_hand[4].value:
                score = 8
            else:
                score = 3
        elif (hand.cards_in_hand[1].value == hand.cards_in_hand[2].value and hand.cards_in_hand[1].value == hand.cards_in_hand[3].value):
            score = 3
        elif (hand.cards_in_hand[2].value == hand.cards_in_hand[3].value and hand.cards_in_hand[2].value == hand.cards_in_hand[4].value):
            if hand.cards_in_hand[0].value == hand.cards_in_hand[1].value:
                score = 8
            else:
                score = 3
        elif (hand.cards_in_hand[3].value == hand.cards_in_hand[4].value) and (hand.cards_in_hand[3].value >= 11 and hand.cards_in_hand[4].value >= 11):
            if (hand.cards_in_hand[0].value == hand.cards_in_hand[1].value) or (hand.cards_in_hand[1].value == hand.cards_in_hand[2].value):
                score = 2
            else:
                score = 1
        elif (hand.cards_in_hand[2].value == hand.cards_in_hand[3].value) and (hand.cards_in_hand[2].value >= 11 and hand.cards_in_hand[3].value >= 11):
            if (hand.cards_in_hand[0].value == hand.cards_in_hand[1].value):
                score = 2
            else:
                score = 1
        elif (hand.cards_in_hand[1].value == hand.cards_in_hand[2].value) and (hand.cards_in_hand[1].value >= 11 and hand.cards_in_hand[2].value >= 11):
            if (hand.cards_in_hand[3].value == hand.cards_in_hand[4].value):
                score = 2
            else:
                score = 1
        elif (hand.cards_in_hand[0].value == hand.cards_in_hand[1].value) and (hand.cards_in_hand[0].value >= 11 and hand.cards_in_hand[1].value >= 11):
            if (hand.cards_in_hand[2].value == hand.cards_in_hand[3].value) or (hand.cards_in_hand[3].value == hand.cards_in_hand[4].value):
                score = 2
            else:
                score = 1
        elif (hand.cards_in_hand[0].suit == hand.cards_in_hand[1].suit and hand.cards_in_hand[1].suit == hand.cards_in_hand[2].suit and hand.cards_in_hand[2].suit == hand.cards_in_hand[3].suit and hand.cards_in_hand[3].suit == hand.cards_in_hand[4].suit):
            score = 5
        return self.score + score
                    
    def card_switcher(self, game, reptotal):
        rep = []
        if (reptotal > 5):
            reptotal = 5
        while (len(rep) < reptotal):
            repnum = int(input('What card do you want to replace? (1 - 1st card, etc.) '))
            if (repnum > 5):
                repnum = 5
            rep.append(repnum - 1)
            rep.reverse()
        for i in range(reptotal):
            game.game_hand.pullCard(rep[i], game.game_deck)
        game.game_deck.shuffle()
        game.game_hand.fillHand(game.game_deck)

        
class game_driver(video_poker):
    def __init__(self):
        super().__init__(0)
        self.main_menu(self.score)

    def main_menu(self, score):
        os.system('cls')
        print ('Welcome to video poker!')
        print ('what would you like to do?')
        print ('1. New Game')
        print ('2. Exit')
        choice = input()
        if choice == '1':
            self.game_menu(score)

    def game_menu(self, score):
        os.system('cls')
        game = video_poker(score)
        game.game_hand.sortHand()
        print (game.game_hand)
        s = 'your current score is: ' + str(game.score)
        print (s)
        print ('What would you like to do?')
        print ('1. Get New Hand')
        print ('2. Replace Cards')
        print ('3. Keep Cards')
        choice = input()
        if choice == '1':
            game.game_hand.newHand(5, game.game_deck)
            self.end_menu(game)
        elif choice == '2':
            self.switch_menu(game)
        elif choice == '3':
            self.end_menu(game)

    def switch_menu(self, game):
        os.system('cls')
        print (game.game_hand)
        reptotal = int(input('How many cards do you want to change? '))
        self.card_switcher(game, reptotal)
        self.end_menu(game)

    def end_menu(self, game):
        os.system('cls')
        game.score = game.find_score(game.game_hand)
        print (game.game_hand)
        s = 'your current score is: ' + str(game.score)
        print (s)
        print ('What would you like to do?')
        print ('1. New Game')
        print ('2. Play Again')
        print ('3. Exit')
        option = input()
        if (option == '1'):
            self.game_menu(0)
        elif (option == '2'):
            self.game_menu(game.score)
        
game1 = game_driver()