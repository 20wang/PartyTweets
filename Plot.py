import string
import matplotlib.pyplot as plt

def importScores():
    file = [line.rstrip('\n') for line in open('GovtrackScores.csv')]
    for i in range(0, len(file)):
        file[i] = file[i].split(',')
    del file[0]

    scores = []
    for line in file:
        scores.append([line[8][2:-1], line[3]])

    return scores


def importHandles():
    file = [line.rstrip('\n') for line in open('legislators-current.csv')]
    for i in range(0, len(file)):
        file[i] = file[i].split(',')
    del file[0]

    handles = []
    for line in file:
        handles.append([line[0], line[18]])

    return handles


def importTweets():
    file = [line.rstrip('\n') for line in open('ExtractedTweets.csv')]
    for i in range(0, len(file)):
        file[i] = file[i].split(',')
    del file[0]

    return file


def importWords():
    file = [line.rstrip('\n') for line in open('ScoredWords')]
    for i in range(0, len(file)):
        file[i] = file[i].split(',')

    return file


def scoreReps(scores, handles, tweets, words):
    chars = string.punctuation + '…'
    reps = []

    for h in handles:
        party = ''
        tempFile = []
        score = 0

        ideology = '-1'
        for s in scores:
            if s[0] == h[0]:
                ideology = s[1]

        for t in tweets:
            if t[0] == 'Democrat' or t[0] == 'Republican':
                if h[1] == t[1]:
                    tempFile.append(t)
                    party = t[0]

        if len(tempFile) != 0:
            print(h[0])
            tempWords = []
            for line in tempFile:
                for i in range(len(line) - 1, 1, -1):
                    tempList = []
                    tempStr = line[i]
                    for c in range(len(chars)):
                        tempStr = tempStr.replace(chars[c], '')
                    tempStr = tempStr.lower()
                    tempList = tempStr.split()

                    for word in tempList:
                        tempWords.append(word)

            for x in words:
                for w in tempWords:
                    if w == x[0]:
                        score += float(x[1])

            rep = [h[0], h[1], party, ideology, str(score)]
            reps.append(rep)

            f = open('TwitterReps', 'a')
            f.write(rep[0] + ',' + rep[1] + ',' + rep[2] + ',' + rep[3] + ',' + rep[4] + '\n')
            f.close()

    return reps


# help for this method came from:
# https://stackoverflow.com/questions/4270301/matplotlib-multiple-datasets-on-the-same-scatter-plot
def plot():
    file = [line.rstrip('\n') for line in open('TwitterReps')]
    for i in range(0, len(file)):
        file[i] = file[i].split(',')

    demX = []
    demY = []
    repX = []
    repY = []

    for line in file:
        if line[2] == 'Democrat':
            demX.append(float(line[3]))
            demY.append(float(line[4])/10000)
        if line[2] == 'Republican':
            repX.append(float(line[3]))
            repY.append(float(line[4]) / 10000)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    ax1.scatter(demX, demY, s=10, c='b', label='Democrats')
    ax1.scatter(repX, repY, s=10, c='r', label='Republicans')
    plt.legend(loc='upper left')
    plt.show()


if __name__ == '__main__':
    """
    scores = importScores()
    handles = importHandles()
    tweets = importTweets()
    words = importWords()
    reps = scoreReps(scores, handles, tweets, words)
    """

    plot()
