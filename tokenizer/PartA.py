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

def tokenizeString(words: str) -> list:
    lst = []
    # Create regular expression that would match all non-alphanumeric characters
    p = re.compile(r'[^a-zA-Z0-9 -]')
    lineEdit = p.sub(" ", words)
    # Splits based on regular expression convert all alphabetical characters to lowercase
    temp = lineEdit.lower().split()
    # Removes the "" element that is at the end of each line
    if "" in temp:
        temp.remove("")
    lst.extend(temp)
    return lst

def removeStopwords(lst: list) -> list:
    newList = lst.copy()
    filePath = "stopwords.txt"
    stopLst = tokenize(filePath)
    for token in lst:
        if token in stopLst:
            newList.remove(token)
    return newList

"""
This runs on linear time O(n) in proportion to how many
elements are in list "lst". This is because the function
uses a for loop that increments through the list once.
"""


def computeWordFrequencies(token_list: list) -> dict:
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


def getFreq(freq: dict) -> list:
    sortedFreq = list()
    # Turn the dictionary "freq" into a list of tuples to make sorting easier.
    tupleList = [(v, k) for k, v in freq.items()]
    # Sorting and iterating through the sorted list.
    counter = 0
    for value, key in sorted(tupleList, key=lambda x: (-x[0], x[1])):
        if counter == 50:
            break
        sortedFreq.append((value, key))
        counter += 1
    return sortedFreq