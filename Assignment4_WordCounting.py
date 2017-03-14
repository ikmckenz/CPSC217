# This is a program to take a text file and count paragraphs and sentences/words in each paragraph.
# It also counts total words and outputs the most used words.
# Everything is output to a file. 
# It seems to produce output files which are nearly identical to the sample output files, but
# sometimes the word occurences section presents the words in a different order to the examples.


# This takes the file name input and returns the name of the input and output filenames as iFile and oFile.
def finput():
	iFile = input("Input the name of the .in input file: ") 
	oFile = iFile.split(".")
	oFile = oFile[0]+".out"
	print("The name of the output file will be " + oFile)
	return iFile, oFile

# This takes the text string and returns the text split up into a list called paragraph.
# Also returns lenp, which is the length of the paragraph string.
def paragraph(text):
	paragraph = text.split("\n\n")
	lenp = len(paragraph)
	outf.write("# of paragraphs: " + str(lenp) + "\n\n")
	return paragraph, lenp

# This takes the text in a paragraph and splits it into sentences and outputs the number of sentences.
def sentence(sparagraph):
	stext = sparagraph.replace("!", ".")
	stext = stext.replace("?", ".")
	stext = stext.split(".")
	sentences = len(stext) - 1
	outf.write("  # of sentences: " + str(sentences) + "\n")

# This takes the text in a paragraph and splits it into words and outputs the number of words
def word(wparagraph):
	wtext = wparagraph.split(" ")
	numwords = len(wtext)
	outf.write("  # of words: " + str(numwords) + "\n")
	return numwords

# This counts frequency of words, it only takes the original text
def count(text):
	worddic = {}
	# First remove all the punctuation from the text
	ctext = text.replace("?", "")
	ctext = ctext.replace("\n\n", " ")
	ctext = ctext.replace("!", "")
	ctext = ctext.replace(".", "")
	ctext = ctext.replace(";", "")
	ctext = ctext.replace(",", "")
	ctext = ctext.replace("\n", "")
	ctext = ctext.split(" ")
	# Then count the frequency of each word
	for i in ctext:
		if i not in worddic:
			worddic[i] = 1
		else:
			worddic[i] = worddic[i]+1
	biggest = max(worddic.values())
	for i in worddic:
		if worddic[i] == biggest:
			if biggest == 1:
				outf.write('"' + str(i) + '" occurs 1 time\n')
			else:
				outf.write('"' + str(i) + '" occurs ' + str(biggest) + " times\n")


# Okay now that we've defined everything, let's run it!

iFile, oFile = finput() # Ask for user input and set filenames

# Open the input and output files
inf = open(iFile, "r") 
outf = open(oFile, "w")

# Take all the text from the file, format it lowercase, and save it.
text = inf.read()
text = text.lower()


paragraph, lenp = paragraph(text) # Call paragraph function, set paragraph as a list with paragraphs in it
totalwords = 0 # Introduce totalwords counter

# The loop that runs the sentence and word counters for each paragraph
for i in range(lenp):
	outf.write("Paragraph " + str(i+1) + ":\n")
	sparagraph = paragraph[i] # Holds the text of the first paragraph, instead of a list containing all of them.
	wparagraph = paragraph[i]
	sentence(sparagraph) # Call the sentence counter on the first paragraph
	numwords = word(wparagraph) # Call the word counter on the first paragraph
	outf.write("\n")
	totalwords = totalwords + numwords # Add the number of words in this paragraph to totalwords

outf.write("Total # of words: " + str(totalwords) + "\n")
count(text)

inf.close()
outf.close()
