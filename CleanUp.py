if __name__ == '__main__':
    file = [line.rstrip('\n') for line in open('TwitterData')]
    for i in range(0, len(file)):
        file[i] = file[i].split(',')

    for l in range(len(file)-1, 0, -1):
        for x in range(l):
            if file[x][0] == file[l][0]:
                file[x][1] = str(float(file[x][1]) + float(file[l][1]))
                del file[l]

    f = open('ScoredWords', 'w')
    for line in file:
        f.write(','.join(line) + '\n')
    f.close()
