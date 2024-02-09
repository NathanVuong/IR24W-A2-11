import PartA as A
import sys

"""
This is the main function and it runs on O(n + m + plogp + qlogq) time where
n is the file size (number of characters) for file 1, m is the file size for 
file 2, p is the number of unique tokens in file 1, and q is the number of
unique tokens in file 2.
"""
if __name__ == '__main__':
    # Read file paths from command line.
    if len(sys.argv) != 3:
        raise Exception("Please provide 2 inputs.")
    text_file_1 = sys.argv[1]
    text_file_2 = sys.argv[2]

    # Use tokenize from PartA.py to get all tokens.
    # Will take O(n) time based on file size.
    file1_tokens = A.tokenize(text_file_1)
    file2_tokens = A.tokenize(text_file_2)

    # Remove duplicate tokens and sort to make finding intersections more efficient.
    # Will take O(nlogn) time to sort.
    sorted_tokens1 = sorted(list(set(file1_tokens)))
    sorted_tokens2 = sorted(list(set(file2_tokens)))
    tokens1_length = len(sorted_tokens1)
    tokens2_length = len(sorted_tokens2)
    index1 = 0
    index2 = 0

    intersection_list = []
    # Iterate through the sorted lists and list the intersections.
    while index1 < tokens1_length and index2 < tokens2_length:
        if sorted_tokens1[index1] < sorted_tokens2[index2]:
            index1 += 1
        elif sorted_tokens1[index1] > sorted_tokens2[index2]:
            index2 += 1
        else:
            intersection_list.append(sorted_tokens1[index1])
            index1 += 1
            index2 += 1
    print(len(intersection_list))
