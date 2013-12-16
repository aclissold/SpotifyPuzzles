# Cat vs. Dog

from itertools import combinations

results = []

def run_testcase(c, d, votes):

    catlovers = []
    doglovers = []

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

    for vote in votes:
        keep, remove = vote.split(' ')
        if keep[0] == 'C':
            catlovers[int(keep[1:])-1][int(remove[1:])-1] += 1
        elif keep[0] == 'D':
            doglovers[int(keep[1:])-1][int(remove[1:])-1] += 1
        else:
            print 'Vote neither started with C nor D'

    # Find total, assuming catlovers always win
    best = 0
    cat_sum, dog_sum = [0 for i in xrange(c)], [0 for i in xrange(d)]
    for i in xrange(c):
        for j in xrange(d):
            cat_sum[i] += catlovers[i][j]
            dog_sum[j] += catlovers[i][j]

    print 'cat_sum, dog_sum:', cat_sum, dog_sum

    for i in xrange(c):
        for j in xrange(d):
            best += catlovers[i][j]

    print 'Best assuming catlovers:', best

    # Generate permutations
    print 'Dogs:'
    for i in xrange(1, d+1):
        for dog in combinations(range(d), i):
            for j in xrange(1, c+1):
                for cat in combinations(range(c), j):
                    print 'Dog:', dog, 'Cat:', cat
                    gain = 0
                    for m in dog:
                        for n in cat:
                            gain += doglovers[m][n]
                    print 'Stand to gain', gain

    global results
    results.append(catlovers)
    results.append(doglovers)

def main():
    # Parse input
    number_of_testcases = int(raw_input())
    for i in xrange(number_of_testcases):
        global num
        num = i + 1
        data = raw_input()
        c, d, v = data.split(' ')
        c, d, v = int(c), int(d), int(v)
        votes = []
        for i in xrange(v):
            votes.append(raw_input())

        # Run testcase
        run_testcase(c, d, votes)

    # Print results
    for result in results:
        print result

if __name__ == '__main__':
    main()
