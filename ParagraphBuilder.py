import random

#  f.read().splitlines() removed trailing newlines, whereas f.readlines() didn't
with open('latin_dictionary.txt') as f:
	content = f.read().splitlines()

#index starts at zero
#print content[5]
#print ('\n')
#print "Highest index: " + str(len(content)-1) #highest index = len(content) - 1
#print ('\n')
#for item in content:
#	    print item



highIndexList = len(content) - 1
#need validation on these numbers
minWords = 1 #per sentence
maxWords = 15
minSentences = 2 #per paragraph
maxSentences = 5
numParagraphs = 3 #per page

#generate page
page = ''
for v in range(numParagraphs):
	#generate paragraphs
	paragraph = ''
	sentence = ''
	for w in range(random.randint(minSentences,maxSentences)):
		#generate sentences
		for x in range(random.randint(minWords,maxWords)):
			word = content[random.randint(0,highIndexList)]
			if sentence == '':
				word = word.title()
			sentence += word + " "
		paragraph += sentence.strip() + '. '
		sentence = ''
	page += (paragraph.strip() + '\n\n')
	paragraph = ''
print(page)