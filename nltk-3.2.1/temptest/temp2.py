
import argparse
import csv
import math
from collections import defaultdict
import nltk
from nltk.corpus import brown
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tag import UnigramTagger, BrillTaggerTrainer

parser = argparse.ArgumentParser()
#parser.add_argument("-corpus", help="File location for 80-20 split")
parser.add_argument("-cross", action ="store_true", help="do 10 fold cross validation")
parser.add_argument("-et", action="store_true", help="do 80-20 corpus split")
args = parser.parse_args()
print("Using unigram taggers because they are the best. Tagging with most likely tag.")
if (args.et):
	category = "news"
	tagged_tokens = []
	correct_tokens = []
	test_sent = brown.sents(categories=category)[33:]
	uni_tagger = UnigramTagger(brown.tagged_sents(categories=category)[:32])
	correct_tags = brown.tagged_sents(categories=category)[33:]
	#print("correct tags\n")
	#print(str(len(correct_tags[0])))
	for sent in correct_tags:
		for tok, tag in sent:
			correct_tokens.append((tok, tag))
			#print("(%s, %s), " % (tok, tag))
	for sent in test_sent:
		for tok, tag in uni_tagger.tag(sent):
			#print("(%s, %s), " % (tok, tag))
			tagged_tokens.append((tok, tag))

	print(str(len(tagged_tokens)) + " " + str(len(correct_tokens)))
	numBadTags = 0
	confusedTags = defaultdict(tuple)
	for i in range(0, len(tagged_tokens)):
		if (tagged_tokens[i][1] != correct_tokens[i][1]):
			numBadTags +=1
			confusedTags[correct_tokens[i][0]] = (tagged_tokens[i][1], correct_tokens[i][1])
	tagAcc = float(1 - numBadTags/len(tagged_tokens))
	print("Tagger Accuracy for 80-20 Split on Brown corpus using: \n\t" + category + "\n is: " + str(round(tagAcc, 4)))
	# custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
	# tokenized = custom_sent_tokenizer.tokenize(sample_text)

	# print(confusedTags)
	# with open("output.csv", "w") as f:
	# 	writer = csv.writer(f)
	# 	writer.writerows(zip(correct_tokens, tagged_tokens))

	# confMatr = open("confusionMatrix.txt", "w") 
	# for i in range(len(tagged_tokens)):
	# 	confMatr.write(str(tagged_tokens[i]) + "\t" + str(correct_tokens[i]) + "\n")
	# confMatr.close()

elif (args.cross):
	category = "news"
	tagged_tokens = []
	correct_tokens = []
	badTagsList = []
	numCorpora = 44
	for i in range(10):
		crossStart = int(i * numCorpora/10)
		crossEnd = int((i+1) * numCorpora/10)
		test_sent = brown.sents(categories=category)[crossStart:crossEnd]
		backoff_tagger = None
		if (crossStart > 0):
			print("using backup tagger ")
			backoff_tagger = UnigramTagger(brown.tagged_sents(categories=category)[0:crossStart])
		uni_tagger = UnigramTagger(brown.tagged_sents(categories=category)[crossEnd:], model=None, backoff=backoff_tagger)
		correct_tags = brown.tagged_sents(categories=category)[crossStart:crossEnd]
		tempTagged = []
		tempCorrect = []
		
		for sent in test_sent:
			for tok, tag in uni_tagger.tag(sent):
				tempTagged.append((tok, tag))		
		tagged_tokens.extend(tempTagged)

		for sent in correct_tags:
			for tok, tag in sent:
				tempCorrect.append((tok, tag))			
		correct_tokens.extend(tempCorrect)
		
		numBadTags = 0
		for j in range(len(tempTagged)):
			if (tempTagged[j][0] == tempCorrect[j][0]):
				if (tempTagged[j][1] != tempCorrect[j][1]):
					numBadTags +=1
		#badTagsList.append(numBadTags)

		print(str(len(tagged_tokens)) + " " + str(len(correct_tokens)))
		print(badTagsList)
		tagAcc = round(1 - float(numBadTags/len(tempCorrect)), 4)
		badTagsList.append(tagAcc)
		print("Tagger Accuracy for 10 Fold Cross Validation on Brown corpus using: \n\t" + category + "\n\t on fold number : " + str(i) + "\n is " + str(tagAcc))
	
	totalBadTags = sum(badTagsList)
	average = totalBadTags/10
	sumr = 0
	for num in badTagsList:
		sumr += pow((num-average),2)
	stdev = sumr/average
	print("Standard Deviation of all taggers is is " + str(round(stdev, 4)))

else :
	print("****Please pick cross validation or 10 fold options. -help for specfications.*****")
# def process_content():
# 	#defaultTag = DefaultTagger(
#     try:
#         for i in tokenized[:5]:
#             words = nltk.word_tokenize(i)
#             tagged = nltk.pos_tag(words)
#             print(tagged)

#     except Exception as e:
#         print(str(e))

