def checkWords():
    file = [line.rstrip('\n') for line in open('Dictionary')]
    for i in range(0, len(file)):
        file[i] = file[i].split(',')

    dCount = 0
    rCount = 0

    for line in file:
        if int(line[1]) > 0:
            dCount += 1
        if int(line[2]) > 0:
            rCount += 1

    print('Republican Words: ', rCount)
    print('Democratic Words: ', dCount)

def mostPolarized():
    file = [line.rstrip('\n') for line in open('ScoredWords')]
    for i in range(0, len(file)):
        file[i] = file[i].split(',')

    rWords = [['placeholder', 0], ['placeholder', 0], ['placeholder', 0], ['placeholder', 0], ['placeholder', 0],
              ['placeholder', 0], ['placeholder', 0], ['placeholder', 0], ['placeholder', 0], ['placeholder', 0]]
    dWords = [['placeholder', 0], ['placeholder', 0], ['placeholder', 0], ['placeholder', 0], ['placeholder', 0], ['placeholder', 0], ['placeholder', 0], ['placeholder', 0], ['placeholder', 0], ['placeholder', 0]]

    for line in file:
        for w in range(len(rWords)):
            if float(line[1]) > float(rWords[w][1]):
                rWords[w] = line
                break

    for line in file:
        for w in range(len(dWords)):
            if float(line[1]) < float(dWords[w][1]):
                dWords[w] = line
                break

    for word in rWords:
        print(word[0] + ': ' + str(word[1]))

    print()

    for word in dWords:
        print(word[0] + ': ' + str(word[1]))

def repeats():
    file = [line.rstrip('\n') for line in open('TwitterReps')]
    for i in range(0, len(file)):
        file[i] = file[i].split(',')

    for line in range(len(file)):
        for l in range(line + 1, len(file)):
            if file[line][0] == file[l][0]:
                print(file[line][0])

def orderWords():
    file = [line.rstrip('\n') for line in open('ScoredWords')]
    for i in range(0, len(file)):
        file[i] = file[i].split(',')

    orderedWords = [['DEBUG', '0.00']]
    for i in range(len(file)):
        for x in range(len(orderedWords)):
            if float(file[i][1]) <= float(orderedWords[x][1]):
                orderedWords.insert(x-1, file[i])
                print(file[i][0])
                break

    f = open('orderedWords', 'w')
    for line in orderedWords:
        f.write(','.join(line) + '\n')
    f.close()


if __name__ == '__main__':
    mostPolarized()