import re
import sys

"""
This runs on linear time O(n) where n is the number of characters 
in the file. This is because the while loop will increment for each 
line in the file and then call split() which would effectively make
the function iterate over each character.
"""


def tokenize(fname: str) -> list:
    lst = []
    # Create regular expression that would match all non-alphanumeric characters
    p = re.compile(r'[^a-zA-Z0-9 -]')
    with open(fname, 'r') as f:
        line = f.readline()
        while line:
            # Removes all nonalphanumeric characters
            line_edit = p.sub(" ", line)
            # Splits based on regular expression convert all alphabetical characters to lowercase
            temp = line_edit.lower().split()
            # Removes the "" element that is at the end of each line
            if "" in temp:
                temp.remove("")
            lst.extend(temp)
            line = f.readline()
    return lst


"""
This runs on linear time O(n) in proportion to how many
elements are in list "lst". This is because the function
uses a for loop that increments through the list once.
"""


def compute_word_frequencies(token_list: list) -> dict:
    frequencies = {}
    # Increment through lst and increases the word counter for each occurence.
    for word in token_list:
        if word in frequencies:
            frequencies[word] = frequencies[word] + 1
        else:
            frequencies[word] = 1
    return frequencies


"""
This runs on loglinear time O(nlogn) in proportion to the size
of the dictionary "freq". This is because the sorted() algorithm
takes O(nlogn) time and is run on a data structure of the same size as "freq".
"""


def print_freq(freq: dict) -> None:
    # Turn the dictionary "freq" into a list of tuples to make sorting easier.
    tuple_list = [(v, k) for k, v in freq.items()]
    # Sorting and iterating through the sorted list.
    for value, key in sorted(tuple_list, key=lambda x: (-x[0], x[1])):
        print(key + " -> " + str(value))


"""
This is the main function and the time complexity of the program
is O(n + mlogm) where n is the number of characters in the file and
m is the number of unique tokens.
"""
if __name__ == "__main__":
    tokens = tokenize(sys.argv[1])
    freq = compute_word_frequencies(tokens)
    print_freq(freq)
else:
    pass
