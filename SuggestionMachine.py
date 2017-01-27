class SuggestionMachine:
	map = set()
	map_unpacked = dict()
	words_in_dict = ["dania", "brady"]

	def __init__(self):
		self.initialize_map();

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
		if query in self.map:
			print "Found query " + query
		else:
			print "Did you mean " + self.calculate_best_result(query) + "?"

	def calculate_best_result(self, query):
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