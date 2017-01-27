class SuggestionMachine:
	word_map = set()
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
			if word not in self.word_map:
				self.word_map.add(word)
				self.map_unpacked[word] = set()
				for character in word:
					self.map_unpacked[word].add(character)

	def check_existence(self, query):
		if query in self.word_map:
			return True
		return False

	def search_for_value(self, query):
		query = query.lower()
		if self.check_existence(query):
			print "Found query " + query
		else:
			print "Did you mean " + self.get_recommended_word(query) + "?"

	def get_recommended_word(self, query):
		substring, substring_bool = self.calculate_closest_substring(query)
		sim_char_count, sim_char_count_bool = self.calculate_sim_char_count(query)

		if substring_bool:
			return substring
		return sim_char_count

	def calculate_closest_substring(self, query):
		answer = ""
		min_distance_in_length = 10000 # placeholder for "infinity"

		for word in self.word_map:
			if query in word:
				if len(word) - len(query) < min_distance_in_length:
					min_distance_in_length = len(word) - len(query)
					answer = word

		if answer == "":
			return "", False
		return answer, True

	def calculate_sim_char_count(self, query):
		query_map = set()
		for character in query:
			query_map.add(character)

		answer = ""
		common_num = 0
		for word in self.word_map:
			similarity = len(query_map.intersection(self.map_unpacked[word]))
			if similarity > common_num:
				common_num = similarity
				answer = word 

		if answer == "":
			return "", False
		return answer, True

	def print_dictionary(self):
		for result in self.word_map:
			print result