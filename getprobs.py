import sys;
def getProbs(fileName):
    
    file = open(fileName,'r+');
    # Calculate and store each word count in the file
    wordCount={}
    for word in file.read().split():
        if word not in wordCount:
            wordCount[word] = 1
        else:
            wordCount[word] += 1

    # Calculate the total number of words in the file
    totalWords = 0;
    for k,v in wordCount.items():   
        totalWords += v;

    file.close();
   
    #Calculate and store probability of each word in the file
    probWords = {}
    for k,v in wordCount.items():
        prob = ((v * 1.0)/totalWords);
        probWords[k] = prob;

    return probWords, totalWords;

