# Zipf's Song

import Queue

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

    # To compute z[i], scale (total_listens/i) by this value so that
    # the sum of all z[i]'s will add up to the total_listens.
    zipf_constant = float(total_listens /
        sum([total_listens/i for i in xrange(1, n+1)]))

    # Compute each zi and qi
    z, q = [], []
    for i in xrange(1, n+1):
        z.append(zipf_constant * (total_listens/i))
        q.append(f[i-1] / z[i-1])

    # Construct the answer as a priority queue with quality as its keys
    queue = Queue.PriorityQueue()
    for i in xrange(n):
        # Use negative qualities since get() gets the value with the lowest key
        queue.put((-1*q[i], s[i]))

    # Print the results
    for i in xrange(m):
        print queue.get()[1] # get()[0] would return the quality

if __name__ == '__main__':
    main()
