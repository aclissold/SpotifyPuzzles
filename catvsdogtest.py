import catvsdoggraph
import catvsdogbrute

from random import randint
from time import sleep

def main():

    # XXX RANDOM TESTCASES

    total = 0
    for i in xrange(5000):
        c, d, v = randint(1, 20), randint(1, 20), randint(0, 500)
        votes = []
        for j in xrange(v):
            cat = randint(1, c)
            dog = randint(1, d)
            if randint(0, 1):
                votes.append('C' + str(cat) + ' D' + str(dog))
            else:
                votes.append('D' + str(dog) + ' C' + str(cat))
        brute_answer = catvsdogbrute.run_testcase(c, d, votes)
        smart_answer = catvsdoggraph.run_testcase(c, d, votes)
        if brute_answer == smart_answer:
            total += 1
        else:
            pass
        if i % 50 == 0:
            print str(int(100*float(i)/5000)) + '% complete.'
    print str(int(100*float(total)/5000)) + '% accurate.'

    # XXX PARTICULAR TESTCASES

#    c, d, v = 1, 2, 3
#
    #votes = ['C1 D2',
    #         'C1 D2',
    #         'D1 C1']
    #
    #votes = [
    #        'D1 C1',
    #        'C1 D1',
    #        'C1 D1',
    #        'C1 D1'
    #        ]
    #votes = [
    #        'D2 C1',
    #        'D2 C1',
    #        'C1 D1',
    #        'C1 D1',
    #        'D1 C1',
    #        ]
    #votes = [
    #        'C1 D1',
    #        'C1 D1',
    #        'C1 D2',
    #        'D2 C1'
    #        ]
#
#    print
#    for vote in votes:
#        print vote
#    print
#    brute_answer = catvsdogbrute.run_testcase(c, d, votes)
#    smart_answer = catvsdoggraph.run_testcase(c, d, votes)
#    print 'brute-->', brute_answer, '?=', smart_answer, '<-- real'

if __name__ == '__main__':
    main()
