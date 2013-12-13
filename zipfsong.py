def main():
    data = raw_input().split(' ')
    n, m = int(data[0]), int(data[1])
    f, s, z, q = [], [], [], []
    for i in xrange(n):
        data = raw_input().split(' ')
        f.append(int(data[0]))
        s.append(data[1])

    total_listens = float(sum(f)) # a float for use in division equations
    zipf_constant = float(total_listens /
        sum([total_listens/i for i in xrange(1, n+1)]))

    for i in xrange(1, n+1):
        z.append(zipf_constant * (total_listens/i))
        q.append(f[i-1] / z[i-1])

    for i in xrange(n):
        print 'Song', s[i], 'had', f[i], 'listens, but Zipf predicted', z[i], \
            'yielding a quality of', q[i]

if __name__ == '__main__':
    main()
