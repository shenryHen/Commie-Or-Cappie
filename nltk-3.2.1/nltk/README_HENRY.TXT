Henry Shen
Tagger: NLTK 3.2.1
Corpus: Brown
Language: Python 3.5.2 

PRIOR TO RUNNING TAGGER, PLEASE RUN "moveSomething.sh." THIS WILL MOVE THE CORPUS TO WHERE NLTK EXPECTS IT TO BE. 
IF TAGGER CANNOT FIND THE CORPUS, PLEASE MOVE FOLDER ./nltk_data TO Users/[username here]/
NOTE THAT THIS ONLY NEEDS TO BE DONE ONCE, AFTER UNCOMPRESSING THE FILE 

To run tagger:
       $ python3 temp4.py [options]
Options:
	-h            list all options 
	-cross        do 10 fold cross validatoin 
	-et	      do 80-20 corpus split 

Tagger accuracty for both methods, standard deviation for 10 Fold, and common mistagss for 80-20 should print out on stdout after tagger is run.
Contingency tablh 80-20  will be written to a file called confusionMatrix.txt. Formated confusion matrix will be in confusnMatrix_TABLE.csv. Note that temp4.py does not output to this csv file.

Sample Run for 80-20

       $ sh moveSomething.sh
       $ python3 temp4.py -et
       
       Using unigram taggers because they are the best. Tagging with most likely tag.
       99750 99750
       Tagger Accuracy for 80-20 Split on Brown corpus using: 
       	      news
	       is: 0.4318
	      most common mistags
	      Given word   good tag	 bad tag	 number of times mistagged
	      who   WPS    None 267
	      --    --     None 299
	     :;     .	     None 313
	      he    PPS    None 450
	      to    IN     TO	  891
      
Sample Run for 10 Fold 

       $ sh moveSomething.sh # assuming first time, just "out of box" 
       $ python3 temp3.py -cross 
       
       /*.......................*/
       /* more k fold info here */
       /*.......................*/
       Tagger Accuracy for 10 Fold Cross Validation on Brown corpus using: 
       news
       on fold number : 9
	is 0.9048
	Standard Deviation of all taggers is is 0.0097