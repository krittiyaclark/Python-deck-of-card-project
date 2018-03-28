class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __repr__(self):
		return "{} of {}".format(self.value, self.suit)
		# return f"{self.value} of {self.suit}"


class Deck:
	def __init__(self):
		suits = ["Hearts", "Dimonds", "Clubs", "Spades"]
		values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
		self.cards = [Card(value, suit) for suit in suits for value in values]

		# Alternative way
		# for suit in suits:
		# 	for value in values:
		# 		self.cards.append(Card(value, suits))
		# print(self.cards)

	def __repr__(self):
		return f"Deck of {self.count()} cards"

	def count(self):
		return len(self.cards)

	def _deal(self, num):
		count = self.count()
		actual = min([count,num])
		if count == 0:
			raise ValueError("All cards have been dealt")
		cards = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		return cards


d = Deck()
print(d._deal(52))
print(d.count())
print(d._deal(3))


