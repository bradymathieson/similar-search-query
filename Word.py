class Word:
	value = ""
	letter_set = set()

	def __init__(self, word_value):
		value = word_value
		for char in word_value:
			self.letter_set.add(char)

	def __eq__(self, word):
		return self.value == word.value

	def __hash__(self):
		return hash(self.value)