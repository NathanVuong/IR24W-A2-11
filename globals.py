from tokenizer.PartA import getFreq

uniquePages = set()
longestPage = ["N/A", 0]
totalWordFrequency = dict()
icsUciEdu = dict()

def report():
    with open("report.txt", "w") as file:
        file.write("Unique pages found: " + str(len(uniquePages)))
        file.write("Longest page: " + longestPage[0])
        file.write("Length of longest page: " + str(longestPage[1]))
        sortedFrequency = getFreq(totalWordFrequency)
        for index, word in enumerate(sortedFrequency):
            file.write("#" + str(index) + " most common word w/ frequency: " + word[0] + ", " + str(word[1]))
        file.write("Subdomains in ics.uci.edu domain: " + str(len(icsUciEdu)))
        sortedSubdomain = dict(sorted(icsUciEdu.items()))
        for key in sortedSubdomain:
            file.write("Subdomains and their unique pages: " + key + ", " + str(sortedSubdomain[key]))