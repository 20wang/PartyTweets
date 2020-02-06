import string

if __name__ == '__main__':
    chars = string.punctuation + '…'

    file = [line.rstrip('\n') for line in open('ScoredWords')]
    for i in range(0, len(file)):
        file[i] = file[i].split(',')

    words = [line.rstrip('\n') for line in open('words_alpha.txt')]

    testers = ['Gohmert', 'Serrano', 'Sherman', 'Stefanik']

    for tester in testers:
        score = 0
        tempWords = []
        tempFile = [line.rstrip('\n') for line in open(tester)]
        for i in range(0, len(tempFile)):
            tempFile[i] = tempFile[i].split(',')
        for line in tempFile:
            if line[0] == 'Democrat' or line[0] == 'Republican':
                for i in range(len(line) - 1, 1, -1):
                    tempStr = line[i]
                    for c in range(len(chars)):
                        tempStr = tempStr.replace(chars[c], '')
                    tempStr = tempStr.lower()
                    tempList = tempStr.split()

                    for word in tempList:
                        if word in words:
                            tempWords.append(word)
        for x in file:
            for w in tempWords:
                if w == x[0]:
                    score += float(x[1])

        print(tester + ', ' + tempFile[0][0] + ': ' + str(score))
