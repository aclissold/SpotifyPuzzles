# Cat vs. Dog

class Graph:
    '''
    A specialized graph that contains weighted edges and a List of
    any two-node cycles contained within.
    '''
    def __init__(self):
        '''Make a new Graph with an empty adjacency list'''
        self.nodes = {}

    def add_node(self, node):
        '''Add the given node to the graph'''
        # colors: white = unvisited, red = has in and outedges, black = only an
        # in or an outedge
        self.nodes[node] = {}

    def add_edge(self, source, dest):
        '''Add a directed edge or increase the weight of one that exists'''
        if dest not in self.nodes[source]:
            self.nodes[source][dest] = 1
        else:
            # Increment the weight of the edge by 1
            self.nodes[source][dest] += 1


def run_testcase(c, d, votes):

    G = Graph()

    def setup_graph():
        for i in xrange(1, c+1):
            G.add_node('C' + str(i))
        for i in xrange(1, d+1):
            G.add_node('D' + str(i))

        # Add directed edges to the graph based on votes.
        # For example, C1 D1 adds edge C1->D1
        for vote in votes:
            keep, drop = vote.split(' ')
            G.add_edge(keep, drop)

    def color_nodes():
        for node in G.nodes:
            G.nodes[node]['color'] = 'white'

        for source in G.nodes:
            if len(G.nodes[source]) - 1 > 0:
                for dest in G.nodes[source]:
                    if dest != 'color':
                        if G.nodes[dest]['color'] == 'white' and len(G.nodes[dest]) > 1:
                            G.nodes[dest]['color'] = 'red'

        for node in G.nodes:
            if G.nodes[node]['color'] == 'white':
                G.nodes[node]['color'] = 'black'

    def has_conflict():
        for node in G.nodes:
            if G.nodes[node]['color'] == 'red':
                return True
        return False

    # Begin main logic

    setup_graph()
    color_nodes()
    while has_conflict():
        inweight = {}
        outweight = {}
        for i in xrange(1, c+1): inweight['C' + str(i)] = 0
        for i in xrange(1, d+1): inweight['D' + str(i)] = 0
        for i in xrange(1, c+1): outweight['C' + str(i)] = 0
        for i in xrange(1, d+1): outweight['D' + str(i)] = 0

        for source in G.nodes:
            for dest in G.nodes[source]:
                if dest != 'color':
                    inweight[dest] += G.nodes[source][dest]
                    outweight[source] += G.nodes[source][dest]

        ties = []
        worst = (None, float('inf'))
        for node in G.nodes:
            if G.nodes[node]['color'] == 'red':
                if outweight[node] - inweight[node] < worst[1]:
                    worst = (node, outweight[node] - inweight[node])
                    ties = [node]
                elif outweight[node] - inweight[node] == worst[1]:
                    ties.append(node)

        if len(ties) > 1:
            highest = float('-inf')
            to_remove = ''
            for tie in ties:
                if outweight[tie] > highest:
                    highest = outweight[tie]
                    to_remove = tie
            G.nodes[to_remove] = {}
        else:
            if inweight[worst[0]] < outweight[worst[0]]:
                print 'should delete parents instead'
                G.nodes[worst[0]] = {}
            else:
                G.nodes[worst[0]] = {}

        color_nodes()

    ans = 0
    for node in G.nodes:
        for dest in G.nodes[node]:
            if dest != 'color':
                ans += G.nodes[node][dest]

    return ans

def main():
    # Parse input
    results = []
    number_of_testcases = int(raw_input())
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
