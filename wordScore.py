if __name__ == '__main__':
    file = [line.rstrip('\n') for line in open('Dictionary')]
    for i in range(0, len(file)):
        file[i] = file[i].split(',')
    counts = file[len(file) - 1]
    del file[len(file) - 1]

    words = [line.rstrip('\n') for line in open('words_alpha.txt')]
    newFile = []

    for x in range(len(file) - 1, -1, -1):
        print(file[x][0])
        if file[x][0] in words:
            newFile.append([file[x][0], str(1000000 * (float(file[x][2])/float(counts[2]) - float(file[x][1])/float(counts[1])))])
        del file[x]

    f = open('Test', 'w')
    for line in newFile:
        f.write(','.join(line) + '\n')
    f.close()
