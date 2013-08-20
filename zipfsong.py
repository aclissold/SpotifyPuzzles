def main():
    # Read n and m
    data = raw_input()
    n, m = process(data)
    i = 0
    while i < range(n):


def process(data):
    '''Validate and parse the input read from stdin'''
    data = data.strip()
    data = data.split()
    if len(data) != 2:
        print 'Error: you must enter exactly two values.'
        exit(1)
    try:
        n, m = int(data[0]), int(data[1])
    except ValueError:
        print 'Error: values must be integers'
        exit(1)
    if not 1 <= n <= 50000:
        print 'Your first value must be within 1-50000 (inclusive)'
        exit(1)
    if not 1 <= m <= n:
        print 'Your second value must be within 1-(first value) (inclusive)'
        exit(1)
    return n, m

if __name__ == '__main__':
    main()
