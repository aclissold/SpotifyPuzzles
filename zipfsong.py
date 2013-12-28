# Zipf's Song

from operator import itemgetter

def main():

    # Get the values of n, m, f, and s, as stated in the problem
    data = raw_input().split(' ')
    n, m = int(data[0]), int(data[1])
    f, s = [], []
    for i in xrange(n):
        data = raw_input().split(' ')
        f.append(int(data[0]))
        s.append(data[1])

    # total_listens is used in computing the Zipf constant and z[i]'s
    total_listens = float(sum(f)) # a float to avoid integer division

    if total_listens == 0:
        # Nothing more to do
        for i in xrange(m):
            print s[i]
        return

    # To compute z[i], scale (total_listens/i) by this value so that
    # the sum of all z[i]'s will add up to the total_listens.
    zipf_constant = float(total_listens /
        sum([total_listens/i for i in xrange(1, n+1)]))

    # Compute each zi and qi
    z, q = [], []
    for i in xrange(1, n+1):
        z.append(zipf_constant * (total_listens/i))
        q.append(f[i-1] / z[i-1])

    # Construct the answer 'a' as (quality, songname) tuples to sort by quality
    a = []
    for i in xrange(n):
        a.append((q[i], s[i]))

    # Stable-sort the answer so the first songs on the album remain as such
    a = sorted(a, key=itemgetter(0), reverse=True)

    # Print the results
    for i in xrange(m):
        print a[i][1]

if __name__ == '__main__':
    main()
