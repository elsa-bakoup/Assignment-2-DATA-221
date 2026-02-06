#Question 1
import string

with (open(file='sample-file.txt', mode='r') as file):
    lines = file.readlines()

    translator = str.maketrans('', '', string.punctuation)  #creating a translation table to remove the punctuation

    #creating a clean list with just the words in lower case
    clean_list = [
        word.translate(translator)
        for line in lines
        for word in line.lower().split() if sum(c.isalpha() for c in word) >= 2
    ]

    #looping through the list to count the number of each word and storing everything into a dictionary
    word_count = {}
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else :
            word_count[word] = 1

    #sorting the dictionary
    wordCountSorted = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

    #printing everything in the requested format
    for word, count in list(wordCountSorted.items())[:10]:
        print(f"{word} -> {count}")
