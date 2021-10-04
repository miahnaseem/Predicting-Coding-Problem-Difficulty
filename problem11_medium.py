# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal]

# query string
s = "de"

# set of potential strings
set_s = ["dog", "deer", "deal"]

def autocomplete(query, set):
	# Length of query for indexing
	end = len(query)
	autocompletes = []
	
	# Iterate through set of strings
	for i in set_s:
		# compare query to the first `end` letters of the potential autocomplete
		if query == i[:end]:
			autocompletes.append(i)
	return autocompletes

print(autocomplete(s, set_s))