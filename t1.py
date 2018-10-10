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
