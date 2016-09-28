from itertools import permutations

# import all the words
wordfile = open("words.txt")
words = set(x.rstrip() for x in wordfile)
wordfile.close()

# take input
input_word = raw_input("Enter the word to be checked: ").lower()

# find all permutations that can be checked
for n in xrange(2, (len(input_word)/2) + 1):
	print n
	perm_list = (list(permutations(input_word, n)))
	
	for perm in perm_list:
		perm = ''.join(perm)
	
		if perm in words:
			input_word_copy = input_word[:]
			
			# print "current word: ", perm
			# remove the first occurrences of the letters
			for ch in perm:
				input_word_copy = input_word_copy.replace(ch, '', 1)
			
			opp_perm_list = list(permutations(input_word_copy))
			for opp_perm in opp_perm_list:
				opp_perm = ''.join(opp_perm)
				if opp_perm in words:
					print perm, opp_perm