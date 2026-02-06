#Question 3
import string

with (open(file='sample-file.txt', mode='r') as file):
    lines = file.readlines()
    lines = [item for item in lines if item != '\n' and item != ' \n']   #removing all the empty new lines

    chars_to_remove = string.punctuation + string.whitespace
    translator = str.maketrans('', '', chars_to_remove)  #creating a translation table to remove the punctuation


    text = [line.translate(translator).lower() for line in lines]  #cleaning the strings (no whitespace or punctuation)

    duplicates = {}    #empty dictionary to store the values

    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            if text[i] == text[j]:
                if text[i] not in duplicates:
                    duplicates[text[i]] = []
                duplicates[text[i]].append((i + 1, j + 1))

    # number of near-duplicate sets
    print(f"Number of near-duplicate sets: {len(duplicates)}")

    # printing the first two sets
    for idx, (key, pairs) in enumerate(list(duplicates.items())[:2], start=1):
        print(f"\nSet {idx}:")
        for i, j in pairs:
            print(f"Line {i}: {lines[i - 1].strip()}")
            print(f"Line {j}: {lines[j - 1].strip()}")
