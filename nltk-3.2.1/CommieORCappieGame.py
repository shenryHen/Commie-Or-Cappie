from random import randint
import nltk 
from nltk.corpus import state_union
from nltk.tokenize import sent_tokenize, PunktSentenceTokenizer

def getBushLines():
	sample_text = state_union.raw("2002-GWBush.txt")
	train = state_union.raw("2001-GWBush-2.txt")
	custom_sent_tokenIzer = PunktSentenceTokenizer(train)
	cappieLines = custom_sent_tokenIzer.tokenize(sample_text)
	
	return cappieLines

def getMarxLines():
	commie = open("../Manifesto.txt", "r", encoding="utf-8").read()
	commieLines = []
	commieLines = sent_tokenize(commie)
	
	return commieLines

def main():
	capitalistLines = getBushLines()
	communistLines = getMarxLines()
	cont = True
	points = 0
	while (cont == True):
		randPerson = randint(0,1) # 0 for capitalist, 1 for communist
		if (randPerson == 0):
			randLine = randint(0, len(capitalistLines))
			print(capitalistLines[randLine])
		if (randPerson == 1):
			randLine = randint(0, len(communistLines))
			print(communistLines[randLine])

		userInput = int(input("Guess who said it: \n\t 0)George W Bush \t 1)Karl Marx\n"))

		if (userInput == randPerson):
			points+=1
			print("Correct Guess!")
		else:
			print("Incorrect guess")
		userInput = int(input("Keep playing? Press 1 for yes, 2 for no. "))
		if (userInput ==2):
			cont = False

	print("Points", str(points))
	

if __name__ == '__main__':
	main()