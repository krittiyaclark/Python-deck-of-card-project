class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __repr__(self):
		return "{} of {}".format(self.value, self.suit)
		# return f"{self.value} of {self.suit}"

# c = Card("A", "Hearts")
# c2 = Card("10", "Dimonds")
# c3 = Card("K", "Spades")
# print(c, c2, c3)

class Deck:
	def __init__(self):
		suits = ["Hearts", "Dimonds", "Clubs", "Spades"]
		values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
		self.cards = [Card(value, suit) for suit in suits for value in values]

		# Alternative way
		# for suit in suits:
		# 	for value in values:
		# 		self.cards.append(Card(value, suits))
		print(self.cards)

	def __repr__(self):
		return f"Deck of {self.count()} cards"

	def count(self):
		return len(self.cards)

d = Deck()
print(d)