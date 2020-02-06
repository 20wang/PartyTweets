import string


# extracts tweets from csv file
def buildDataset():
    file = [line.rstrip('\n') for line in open('ExtractedTweets.csv')]
    for i in range(0, len(file)):
        file[i] = file[i].split(',')
    del file[0]

    return file


def findWords(file):
    dictionary = []
    coef = 0
    tempStr = ''
    chars = string.punctuation + '…'
    wordCount = ['words:', '0', '0']

    for line in file:
        if len(line) > 1:
            print(line[1])
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
                            print(dictionary[x])
                            wordCount[coef] = str(int(wordCount[coef]) + 1)
                            print(wordCount)
                for word in tempList:
                    if word[0:5] != 'https':
                        dictionary.append([word.lower(), '0', '0'])
                        dictionary[len(dictionary) - 1][coef] = '1'
                        print(dictionary[len(dictionary) - 1])
                        wordCount[coef] = str(int(wordCount[coef]) + 1)
                        print(wordCount)
        coef = 0
    dictionary.append(wordCount)
    return dictionary


def wordScore(file):
    counts = file[len(file) - 1]
    del file[len(file) - 1]

    words = [line.rstrip('\n') for line in open('words_alpha.txt')]
    newFile = []

    x = 0
    while x < len(file):
        if file[x][0] in words:
            print(file[x][0])
            newFile.append([file[x][0], str(
                1000000 * (float(file[x][2]) / float(counts[2]) - float(file[x][1]) / float(counts[1])))])
        del file[x]
        x += 1

    return newFile


def cleanUp(file):
    l = 0
    while l < len(file):
        for x in range(0, l):
            if file[x][0] == file[l][0]:
                file[x][1] = str(float(file[x][1]) + float(file[l][1]))
                del file[l]
        l += 1

    return file


def writeFile(file):
    f = open('TestWords', 'w')
    for line in file:
        f.write(','.join(line) + '\n')
    f.close()


if __name__ == '__main__':
    file = buildDataset()
    dictionary = findWords(file)
    scoredFile = wordScore(dictionary)
    cleanedFile = cleanUp(scoredFile)
    writeFile(cleanedFile)
