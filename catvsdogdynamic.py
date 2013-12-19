def main():

    results = []

    for i in xrange(int(raw_input())):

        data = raw_input()
        c, d, v = data.split(' ')
        c, d, v = int(c), int(d), int(v)

        votes = []
        for v in xrange(v):
            votes.append(raw_input())

        results.append(run_testcase(c, d, votes))

    for result in results:
        print result

def run_testcase(c, d, votes):

    yes, no = {}, {}
    for i in xrange(1, c+1): yes['C'+str(i)] = 0
    for i in xrange(1, c+1): no['C'+str(i)] = 0
    for i in xrange(1, d+1): yes['D'+str(i)] = 0
    for i in xrange(1, d+1): no['D'+str(i)] = 0
    best = [0]

    for i in xrange(1, len(votes)+1):
        keep, remove = votes[i-1].split(' ')

        yes[keep] += 1
        no[remove] += 1

        if yes[keep] > no[keep]:
            best.append(best[i-1] + 1)
        else:
            best.append(best[i-1])

    return best[len(votes)]

if __name__ == '__main__':
    main()
