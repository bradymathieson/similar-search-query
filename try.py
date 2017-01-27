from SuggestionMachine import SuggestionMachine

if __name__ == '__main__':
	search = SuggestionMachine()
	query = raw_input("Enter search query : ")
	search.search_for_value(query)