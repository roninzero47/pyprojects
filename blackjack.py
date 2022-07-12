from random import shuffle
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
suits = ["Hearts", "Diamond", "Clover", "Spade"]
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
game_on = True

'''
Classes
'''

class Card:

    def __init__(self,rank,suit):

        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):

        return self.suit +" of "+ self.rank

class Deck:

    def __init__(self):

        self.all_cards = []

        for rank in ranks:
            for suit in suits:

                self.all_cards.append(Card(rank,suit))

    def shuffle(self):

        shuffle(self.all_cards)

    def __str__(self):

        list_of_cards = " "

        for card in self.all_cards:
            list_of_cards += "\n" + card.__str__()

        return f"The list of cards are: {list_of_cards}"

    def deal_one(self):

        return self.all_cards.pop()

class Chips:

    def __init__(self,total = 1000):

        self.total = total
        self.bet = 0

    def win_bet(self):

        self.total += self.bet

    def lose_bet(self):

        self.total -= self.bet

class Player:

    def __init__(self,name):

        self.name = name
        self.cards = []
        self.value = 0

    def add_card(self,new_card):

        self.value += new_card.value
        self.cards.append(new_card)

    def adjust_ace(self):

        for card in self.cards:
            if card.rank == "Ace" and self.value > 21:

                self.value -= 10

'''
Contains functions in order to run the game.
'''

def bet_chips(chips):

    while True:

        try:
            chips.bet = int(input("How many chips do you want to bet? \n"))

        except ValueError:
            print("Please enter an integer. \n")

        else:
            if chips.bet > chips.total:
                print(f"Bet amount exceeds the total chips in hand \nTotal chips in hand: {chips.total} \n")
            else:
                break

def hit(player,deck):

    player.add_card(deck.deal_one())
    player.adjust_ace()

def hit_or_stand(player,deck):
    global game_on

    while True:

        x = input("Hit or Stand? ").lower()

        if x[0] == 'h':
            hit(player,deck)
            break

        elif x[0] == 's':
            print(f"{player.name} decides to stand! \nDealer's Turn \n")
            game_on = False
            break

        else:
            print("Invalid Input \n")

def show_some(player,dealer):

    print("Dealer's Cards: \n")
    print("<CARD HIDDEN>")
    print(f"{dealer.cards[1]} \n")
    print(f"{player.name}'s Cards:")
    print("",*player.cards, sep = "\n")

def show_all(player,dealer):

    print("Dealer's Cards:")
    print("",*dealer.cards, sep = "\n")
    print(f"Dealer's value: {dealer.value}\n")
    print(f"{player.name}'s Cards:")
    print("",*player.cards, sep = "\n")
    print(f"{player.name}'s value: {player.value} \n")

def player_wins(player,chips):

    print(f"{player.name} Wins!!!")
    chips.win_bet()

def player_busts(player,chips):

    print(f"{player.name} Busts!!!")
    chips.lose_bet()

def dealer_wins(player,chips):

    print("Dealer Wins!!!")
    chips.lose_bet()

def dealer_busts(player,chips):

    print("Dealer Busts!!!")
    chips.win_bet()

def push():

    print("PUSH!!! \nIt's A Tie!!!")

'''
LOGIC PART
'''

if __name__ == '__main__':

    while True:

        print("Welcome to BlackJack!!!")

        game_deck = Deck()
        game_deck.shuffle()

        player_name = input("What's your name: ")

        player = Player(player_name)
        player.add_card(game_deck.deal_one())
        player.add_card(game_deck.deal_one())

        dealer = Player("Dealer")
        dealer.add_card(game_deck.deal_one())
        dealer.add_card(game_deck.deal_one())

        player_chips = Chips()

        bet_chips(player_chips)

        show_some(player,dealer)

        while game_on:

            hit_or_stand(player,game_deck)

            show_some(player,dealer)

            if player.value > 21:

                player_busts(player,player_chips)
                game_on = False

        if player.value <= 21:

            while dealer.value < 17:

                hit(dealer,game_deck)

            show_all(player,dealer)

            if dealer.value > 21:

                dealer_busts(player,player_chips)

            elif dealer.value > player.value:

                dealer_wins(player,player_chips)

            elif dealer.value < player.value:

                player_wins(player,player_chips)

            else:

                push()

        #To ask player to play again.

        x = input("Do you want to play again? \nYes or No? ").lower()

        if x[0] == 'y':
            game_on = True

        elif x[0] == 'n':
            print("Ciao")
            break

        else:
            print("Invalid Input")