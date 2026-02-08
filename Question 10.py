#Question 10
def find_lines_containing(filename, keyword):
    import string

    keyword_lower = keyword.lower()      #converting the keyword to lowercase to make it case unsensitive
    matching_lines = []       #creating a list to append all the matching lines and the line numbers

    with open(filename, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):    #starting at line number 1
            # removing punctuation and making the line lowercase
            clean_line = line.translate(str.maketrans('', '', string.punctuation)).lower()

            if keyword_lower in clean_line:        #checking to see if the keyword is in the line
                matching_lines.append((line_number, line.rstrip('\n')))  # appending matching lines and lines numbers to the designated list

    # printing the requested information in the requested format
    print(f"Number of matching lines: {len(matching_lines)}")
    print("First 3 matching lines:")
    for line_number, txt in matching_lines[:3]:
        print(f"{line_number}: {txt}")

    return matching_lines    #return the list

