# Train.py trains the algorithm by extracting the words from tweets
# 2-6-2020
__author__ = '20wang'


import string


# extracts tweets from csv file
def buildDataset():
    file = [line.rstrip('\n') for line in open('ExtractedTweets.csv')]
    for i in range(0, len(file)):
        file[i] = file[i].split(',')
    del file[0]

    return file


# gets words from tweets, records frequency of each word for Democrats and Republicans
def findWords(file):
    dictionary = []
    coef = 0
    tempStr = ''
    chars = string.punctuation + '…'
    wordCount = ['words:', '0', '0']

    for line in file:
        if line[0] == 'Democrat':
            coef = 1
        if line[0] == 'Republican':
            coef = 2
        if coef != 0:
            for i in range(len(line) - 1, 1, -1):
                tempStr = line[i]
                for c in range(len(chars)):
                    tempStr = tempStr.replace(chars[c], '')
                tempList = tempStr.split()
                for x in range(len(dictionary)):
                    for word in tempList:
                        if word.lower() == dictionary[x][0]:
                            dictionary[x][coef] = str(int(dictionary[x][coef]) + 1)
                            tempList.remove(word)
                            wordCount[coef] = str(int(wordCount[coef]) + 1)
                for word in tempList:
                    if word[0:5] != 'https':
                        dictionary.append([word.lower(), '0', '0'])
                        dictionary[len(dictionary) - 1][coef] = '1'
                        wordCount[coef] = str(int(wordCount[coef]) + 1)
        coef = 0
    dictionary.append(wordCount)

    return dictionary


# assigns scores to words based on frequency for members of each party (- if Democrat, + if Republican)
def wordScore(file):
    counts = file[len(file) - 1]
    del file[len(file) - 1]

    words = [line.rstrip('\n') for line in open('words_alpha.txt')]
    newFile = []

    for x in range(len(file)):
        if file[x][0] in words:
            newFile.append([file[x][0],
                            str(1000000 * (float(file[x][2]) / float(counts[2]) -
                                           float(file[x][1]) / float(counts[1])))])

    return newFile


# removes duplicates in the scored words, caused by flaws in the findWords method
# "if you can't tie a knot, tie a lot"
def cleanUp(file):
    l = 0
    while l < len(file):
        for x in range(0, l):
            if file[x][0] == file[l][0]:
                file[x][1] = str(float(file[x][1]) + float(file[l][1]))
                del file[l]
        l += 1

    return file


# writes the list of words to a csv file
def writeFile(file):
    f = open('ScoredWords', 'w')
    for line in file:
        f.write(','.join(line) + '\n')
    f.close()


# main method
if __name__ == '__main__':
    file = buildDataset()
    dictionary = findWords(file)
    scoredFile = wordScore(dictionary)
    cleanedFile = cleanUp(scoredFile)
    writeFile(cleanedFile)
