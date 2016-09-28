from itertools import permutations

# import all the words
wordfile = open("words.txt")
words = list(x.rstrip() for x in wordfile)

# take input
input_word = raw_input("Enter the word to be checked: ")

# find all permutations that can be checked
for n in xrange(2, (len(input_word)/2) + 1):
	perm_list = (list(permutations(input_word, n)))
	
	for perm in perm_list:
		perm = ''.join(perm)
	
		if perm in words:
			wrd_cpy = input_word[:]
			
			# remove the first occurrences of the letters
			for ch in perm:
				wrd_cpy = wrd_cpy.replace(ch, '', 1)
			
			opp_perm_list = 
			if wrd_cpy in words:
				print perm, wrd_cpy