#Referenced from https://pycarddeck.readthedocs.io/en/latest/examples/poker.html
import pyCardDeck 
from pyCardDeck.cards import PokerCard


def generate_initial_deck():
		cards=[]
		category_of_card = ["Hearts","Spades","Clubs","Diamonds"]
		number_of_card= {'1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine','10':'Ten','J':'Jack','Q':'Queen','K':'King'}

		for i in category_of_card:
			for k,v in number_of_card.items():
				cards.append((k,i))
		return cards

class PokerTable:
	
	def __init__(self, players):
		self.players = list(range(1,players))
		self.deck = pyCardDeck.Deck(cards=generate_initial_deck(),name='Poker Game',reshuffle=False)
		self.table_cards=[]
		self.hand = []
		print("This is a poker table with {} players".format(players))


	def texas_holdem(self):
		"""Basic Texas Hold'em game structure"""
		print("Starting a round of Texas Hold'em")
		self.deck.shuffle()
		self.draw_cards(2)
		
	def draw_cards(self, number):
		card = []
		for _ in range(0, number):
			for player in self.players:
				card = self.deck.draw()
				player.append(card)
			print("Dealt {} to player {}".format(card, player))

		return cards

print(generate_initial_deck())
PT = PokerTable(5)
print(PT.draw_cards(5))
