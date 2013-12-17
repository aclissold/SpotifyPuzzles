# Cat vs. Dog

from itertools import combinations

def run_testcase(c, d, votes):

    catlovers, doglovers = [], []
    best = 0

    # Set up the 2D arrays (rows represent keeps)
    for i in xrange(c):
        row = []
        for i in xrange(d):
            row.append(0)
        catlovers.append(row)
    for i in xrange(d):
        col = []
        for i in xrange(c):
            col.append(0)
        doglovers.append(col)

    # Populate the arrays from the votes
    for vote in votes:
        keep, remove = vote.split(' ')
        if keep[0] == 'C':
            catlovers[int(keep[1:])-1][int(remove[1:])-1] += 1
        else:
            doglovers[int(keep[1:])-1][int(remove[1:])-1] += 1

    # Assume catslovers win
    for i in xrange(c):
        for j in xrange(d):
            best += catlovers[i][j]

    # Generate combinations to find contradictions
    for i in xrange(1, d+1):
        print 'Step', i, 'of', d
        for dog in combinations(range(d), i):
            for j in xrange(1, c+1):
                for cat in combinations(range(c), j):
                    new = 0
                    for m in dog:
                        for n in cat:
                            new += doglovers[m][n]
                    if new > best:
                        best = new

    return best

def main():
    # Parse input
    number_of_testcases = int(raw_input())
    results = []
    for i in xrange(number_of_testcases):
        data = raw_input()
        c, d, v = data.split(' ')
        c, d, v = int(c), int(d), int(v)
        votes = []
        for i in xrange(v):
            votes.append(raw_input())

        # Run testcase
        results.append(run_testcase(c, d, votes))

    # Print results
    for result in results:
        print result

if __name__ == '__main__':
    main()
