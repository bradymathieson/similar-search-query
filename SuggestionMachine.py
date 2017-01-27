class SuggestionMachine:
	map = set()
	map_unpacked = dict()
	words_in_dict = set()

	def __init__(self):
		self.load_dictionary()
		self.initialize_map()

	def load_dictionary(self):
		f = open('google-10000-english-no-swears.txt', 'r')
		content = f.readlines()
		for line in content:
			self.words_in_dict.add(line.strip().lower())

	def initialize_map(self):
		for word in self.words_in_dict:
			if word not in self.map:
				self.map.add(word)
				self.map_unpacked[word] = set()
				for character in word:
					self.map_unpacked[word].add(character)

	def check_existence(self, query):
		if query in self.map:
			return True
		return False

	def search_for_value(self, query):
		query = query.lower()
		if self.check_existence(query):
			print "Found query " + query
		else:
			print "Did you mean " + self.calculate_sim_char_count(query) + "?"

	def calculate_sim_char_count(self, query):
		query_map = set()
		for character in query:
			query_map.add(character)

		answer = ""
		common_num = 0
		for word in self.map:
			similarity = len(query_map.intersection(self.map_unpacked[word]))
			if similarity > common_num:
				common_num = similarity
				answer = word 

		return answer

	def print_dictionary(self):
		for result in self.map:
			print result