"""attempt to read a book and look for stuff"""

class WordNode():
	def __init__(self, word, leftword=None, rightword = None):
		self.word = word
		self.leftword = leftword
		self.rightword = rightword
		self.wordcount = 1

	def __repr__(self):
		if self.leftword == None:
			left = "No Left Word "
		else:
			left = " - left Exists "
		if self.rightword == None:
			right = " No Right Word "
		else:
			right = "- right Exists"
		msg = self.word + left + right
		return msg

	def add_word(self, word):
		new_word = WordNode(word)
		return new_word

	def insert_left_node(self, new_left_node):
		if self.leftword.rightword != None:  # check to see if the node we are inserting to has a right word
			is_there_a_right_word = True # if it does set the flag to True
			compare_right = self.leftword.rightword.word #Also set the word in that right node to the string
		else:
			is_there_a_right_word = False  #if there is no right word, then set it to False


		new_left_node.leftword = self.leftword #since we're inserting a left node, we know that the word value is less than self.word.  Point the left pointer on the new word to the leftword
		self.leftword = new_left_node # Change the existing work to point at the left side do the new word.

		if is_there_a_right_word:  #The left pointer is taken care of, now we need to see if the right pointer needs to point at the right pointer for the left child.
			if compare_right > new_left_node.word: #if the compare_right word is greater than the word for the new node, then the new node rightword should point to it.
				new_left_node.rightword = new_left_node.leftword.rightword # The right node for the left child should point branch off this new node.
				new_left_node.leftword.rightword = None
			else:
				new_left_node.rightword = None

	def insert_right_node(self, new_right_node):
		if self.rightword.leftword != None:
			is_there_a_left_word = True
			compare_left = self.rightword.leftword.word
		else:
			is_there_a_left_word = False


		new_right_node.rightword = self.rightword
		self.rightword = new_right_node
		#print(new_right_node)
		#print("in new_right_node")
		if is_there_a_left_word:
			if compare_left < new_right_node.word:
				new_right_node.leftword = new_right_node.rightword.leftword

				new_right_node.rightword.leftword = None
			else:
				new_right_node.leftword = None





	def add_node(self, startnode, nodeword):  #The first time through this is passed the firstnode which has "may" and no children.
		if startnode.word == nodeword:  #if the node = the passed word, then add to the nodecount
			startnode.wordcount += 1
			#print("added 1 to " + nodeword)
		elif nodeword < startnode.word:  # then it needs to go to the left
			#print("L72 Going Left with " + nodeword + " compared to " + startnode.word)
			if startnode.leftword == None: #check to see if there is a node on the left.  If not, add it there.
				startnode.leftword = startnode.add_word(nodeword)
				#print("L75 added on the left - >" + nodeword)
			else: #Go Left
			 	self.add_node(startnode.leftword, nodeword)
				
		else:
			#print("L83 Going right! with " + nodeword + " compared to " + startnode.word)
			if startnode.rightword == None:
				startnode.rightword = startnode.add_word(nodeword)
				#print("L86 added on the right -> " + nodeword)
			else: #Go rigth
			 	self.add_node(startnode.rightword, nodeword)
				


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
		print(word + " appears (in ==) " + str(firstnode.wordcount) + " times")
		return
	if firstnode.leftword != None and firstnode.leftword.word == word: 
		print(word + " appears (in leftword)" + str(firstnode.leftword.wordcount) + " times")
		return
	elif firstnode.rightword != None and firstnode.rightword.word == word:  #we're done here
		print(word + " appears (in rightword)" + str(firstnode.rightword.wordcount) + " times")
		return

	if firstnode.leftword != None and firstnode.leftword.word <= word: #go right
		if firstnode.rightword != None and firstnode.rightword.word > word: # it doesn't exist
			if firstnode.leftword == None:
				print(word + " doesn't exist")
				return
			else: #go left
				#print("in the else statement line 59")
				find_a_word(firstnode.leftword, word)
				return

		else:
			if firstnode.rightword != None:
				print("going right with " + firstnode.rightword.word + " searching for " + word)
				find_a_word(firstnode.rightword, word)
			else: #go left
				find_a_word(firstnode.leftword, word)
	elif firstnode.leftword != None:
		print("going left with " + firstnode.leftword.word  + " searching for " + word)
		find_a_word(firstnode.leftword, word)
	else:
		print("Word not found")
		return


		




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
filename = "Alice-short.txt"
words_list = count_words(filename)
valid_string = "abcdefghijlmnopqrstuvwxyz-ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "'"
firstnode = WordNode("may")
print(firstnode)
print(firstnode.leftword)
print(firstnode.rightword)
print(firstnode.word)

#print(words_list[100] + " " + words_list [1000] + " " + words_list[1])
charcount = 1

for oneword in words_list:
	newstring = ""
	for char in oneword:
		if char in valid_string:
			newstring += char
	charcount += 1
	#print(charcount)
	#print("Calling add_node with " + newstring)		
	firstnode.add_node(firstnode, newstring.lower())


#for i in range(1,20):
#	print(words_list[i])

traverse_word_tree(firstnode)

active = True

while active:
	search_term = input("What word would you like to find? ")
	if search_term == "quit":
		active = False
	else:
		find_a_word(firstnode, search_term.lower())
		print("\n")


