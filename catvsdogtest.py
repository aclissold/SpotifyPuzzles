import catvsdogdynamic
import catvsdogbrute

from random import randint
from time import sleep

def main():
    total = 0
    for i in xrange(500):
        c, d, v = randint(1, 7), randint(1, 7), randint(0, 500)
        votes = []
        for j in xrange(v):
            cat = randint(1, c)
            dog = randint(1, d)
            if randint(0, 1):
                votes.append('C' + str(cat) + ' D' + str(dog))
            else:
                votes.append('D' + str(dog) + ' C' + str(cat))
        brute_answer = catvsdogbrute.run_testcase(c, d, votes)
        smart_answer = catvsdogdynamic.run_testcase(c, d, votes)
        print brute_answer, '?=', smart_answer
        if brute_answer == smart_answer:
            total += 1
        if i % 5 == 0:
            print str(int(100*float(i)/500)) + '% complete.'
    print str(int(100*float(total)/500)) + '% accurate.'

    #brute_answer = catvsdogbrute.run_testcase(
    #        1, 2, ['C1 D1', 'C1 D1', 'C1 D2', 'D2 C1'])
    #smart_answer = catvsdogdynamic.run_testcase(
    #        1, 2, ['C1 D1', 'C1 D1', 'C1 D2', 'D2 C1'])
    #print brute_answer, smart_answer

if __name__ == '__main__':
    main()
