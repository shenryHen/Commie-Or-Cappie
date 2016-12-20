from random import randint

#482 lines for communist
# 498 lines for bush


def getBushLines():
	cappieLines = []
	cappie = open("./BushFinal.txt", "r", encoding="utf-8")
	for line in cappie:
		cappieLines.append(line)
	#print(cappieLines)	
	return cappieLines

def getMarxLines():
	commie = open("./MarxFinal.txt", "r", encoding="utf-8")
	commieLines = []
	for line in commie:
		commieLines.append(line)
	#print()
	return commieLines

def main():
	capitalistLines = getBushLines()
	communistLines = getMarxLines()
	print("lenght of capitalist lines ",len(capitalistLines), "length of communist lines ", len(communistLines))
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