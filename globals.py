from tokenizer.PartA import getFreq

uniquePages = set()
allPages = list()
longestPage = ["N/A", 0]
totalWordFrequency = dict()
icsUciEdu = dict()

def report():
    filePath = "report.txt"
    with open(filePath, "w") as file:
        file.write("Unique pages found: " + str(len(uniquePages)) + "\n")
        file.write("All pages found: " + str(len(allPages)) + "\n")
        file.write("Longest page: " + longestPage[0] + "\n")
        file.write("Length of longest page: " + str(longestPage[1]) + "\n")
        sortedFrequency = getFreq(totalWordFrequency)
        for index, word in enumerate(sortedFrequency):
            file.write("#" + str(index + 1) + " most common word w/ frequency: " + word[0] + ", " + str(word[1]) + "\n")
        file.write("Subdomains in ics.uci.edu domain: " + str(len(icsUciEdu)) + "\n")
        sortedSubdomain = dict(sorted(icsUciEdu.items()))
        for key in sortedSubdomain:
            file.write("Subdomains and their unique pages: " + key + ", " + str(sortedSubdomain[key]) + "\n")