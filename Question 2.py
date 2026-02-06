#Question 2
import string

with (open(file='sample-file.txt', mode='r') as file):
    lines = file.readlines()

    translator = str.maketrans('', '', string.punctuation)   #creating a translation table to remove the punctuation

    # creating a clean list with just the words in lower case
    clean_list = [
        word.translate(translator)
        for line in lines
        for word in line.lower().split() if sum(c.isalpha() for c in word) >= 2
    ]

    bigrams = [(clean_list[i], clean_list[i+1]) for i in range(len(clean_list)-1)]  #creating a list of bigram as tuple with each word and the following one (using a tuple)

    bigramsCount = {}   #empty dictionary to store the values

    #using a loop to count each bigrams and storing everything into a dictionary
    for bigram in bigrams:
        if bigram in bigramsCount:
            bigramsCount[bigram] += 1
        else:
            bigramsCount[bigram] = 1

     # sorting the dictionary
    bigramCountSorted = dict(sorted(bigramsCount.items(), key=lambda item: item[1], reverse=True))
    first_5 = dict(list(bigramCountSorted.items())[:5])

    # printing everything in the requested format
    for (w1, w2), count in first_5.items():
        print(f"{w1} {w2} -> {count}")