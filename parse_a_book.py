"""attempt to read a book and look for stuff"""

class WordNode():
	def __init__(self, word, leftword=None, rightword = None):
		self.word = word
		self.leftword = leftword
		self.rightword = rightword
		self.wordcount = 1

	def __repr__(self):
		return self.word

	def add_word(self, word):
		new_word = WordNode(word)
		return new_word

	def find_word(self, startnode, nodeword):
		if startnode.word == nodeword:
			startnode.wordcount += 1
		elif startnode.word > nodeword:  # then it needs to go to the left
			if startnode.leftword == None:
				startnode.leftword = startnode.add_word(nodeword)
			elif startnode.leftword.word > nodeword:
				newnode = self.add_word(nodeword)
				newnode.leftword = startnode.leftword  # this part needs work
				startnode.leftword = newnode
			else:
				self.find_word(startnode.leftword, nodeword)
		else:
			if startnode.rightword == None:
				startnode.rightword = startnode.add_word(nodeword)
			elif startnode.rightword.word < nodeword:
				newnode = self.add_word(nodeword)
				newnode.rightword = startnode.rightword
				startnode.rightword = newnode
			else:
				self.find_word(startnode.rightword, nodeword)			


def traverse_word_tree(firstnode):
	if firstnode.leftword != None: 
		traverse_word_tree(firstnode.leftword) #keep going left
	if firstnode.rightword != None: # go right
		traverse_word_tree(firstnode.rightword)
	else:  #means we have hit a null node
		pass
	print(firstnode.word + " " + str(firstnode.wordcount))
	

def find_a_word(firstnode, word):
	if firstnode.word == word:
		print(word + " appears " + str(firstnode.wordcount))
		return
	if firstnode.leftword != None and firstnode.leftword.word == word: 
		print(word + " appears " + str(firstnode.wordcount))
		return
	elif firstnode.rightword != None and firstnode.rightword.word == word:  #we're done here
		print(word + " appears " + str(firstnode.wordcount))
		return

	if firstnode.leftword != None and firstnode.leftword.word <= word: #go right
		if firstnode.rightword != None and firstnode.rightword.word > word: # it doesn't exist
			if firstnode.leftword == None:
				print(word + " doesn't exist")
				return
			else: #go left
				print("in the else statement line 59")
				find_a_word(firstnode.leftword, word)
				return

		else:
			if firstnode.rightword != None:
				print("going right with " + firstnode.rightword.word + " searching for " + word)
				find_a_word(firstnode.rightword, word)
			else: #go left
				find_a_word(firstnode.leftword, word)
	else:
		if firstnode.leftword != None:
			print("going left with " + firstnode.leftword.word  + " searching for " + word)
			find_a_word(firstnode.leftword, word)


		




def count_words(filename):
	try:
		with open(filename, encoding='utf-8') as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		pass
		#msg = "Sorry, the file " + filename + " does not exist."
		#print(msg)
	else:
		# count the words in the file
		words = contents.split()
		return words

		#num_words = len(words)
		#alice_count = 0
		#jo_count = 0
		#ishmael_count = 0
		#for word in words:
		#	if word == "Alice":
		#		alice_count += 1
		#	if word == "Jo":
		#		jo_count += 1
		#	if word == "Ahab":
		#		ishmael_count += 1

		#print(filename + " has " + str(num_words) + " words")
		#print(filename + " has " + str(alice_count) + " Alice references and " + str(jo_count) + " Jo references and " + str(ishmael_count) + " Ahab references.")

#filenames = ["Alice.txt", "moby_dick.txt", "little_women.txt", "siddhartha.txt"]
words_list = []
filename = "Alice.txt"
words_list = count_words(filename)
valid_string = "abcdefghijlmnopqrstuvwxyz-" + "'"
firstnode = WordNode("may")
print(firstnode)
print(firstnode.leftword)
print(firstnode.rightword)
print(firstnode.word)

#print(words_list[100] + " " + words_list [1000] + " " + words_list[1])

for oneword in words_list:
	newstring = ""
	for char in oneword:
		if char in valid_string:
			newstring += char

	firstnode.find_word(firstnode, newstring)


print(firstnode)
print(firstnode.leftword)
print(firstnode.rightword)
print(firstnode.word)
print(firstnode.wordcount)
#find_a_word(firstnode, "whale")
traverse_word_tree(firstnode)