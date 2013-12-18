import readline

def main():
    data = raw_input()

    c, d, v = data.split(' ')
    c, d, v = int(c), int(d), int(v)
    yes, no = {}, {}
    for i in xrange(1, c+1): yes['C'+str(i)] = 0
    for i in xrange(1, c+1): no['C'+str(i)] = 0
    for i in xrange(1, d+1): yes['D'+str(i)] = 0
    for i in xrange(1, d+1): no['D'+str(i)] = 0
    votes = []
    best = [0]

    for v in xrange(v):
        votes.append(raw_input())

    for i in xrange(1, v+2):
        keep, remove = votes[i-1].split(' ')

        yes[keep] += 1
        no[remove] += 1

        if yes[keep] - no[keep] > 0:
            best.append(best[i-1] + 1)
        else:
            best.append(best[i-1])

        print best[i]

if __name__ == '__main__':
    main()
