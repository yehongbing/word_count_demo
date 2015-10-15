__author__ = 'HB_Y'

def word_frequecy_count(str):
    # initialize a dictionary data structure to store the word frequency
    wordcount = {}
    for word in str.split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    return wordcount
