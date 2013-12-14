# Cat vs. Dog

results = []

class Graph:
    '''
    A specialized graph that contains weighted edges and a List of
    any two-node cycles contained within.
    '''
    def __init__(self):
        '''Make a new Graph with an empty adjacency list'''
        self.nodes = {}
        self.cycles = []

    def add_node(self, node):
        '''Add the given node to the graph'''
        self.nodes[node] = {}

    def add_edge(self, source, dest):
        '''Add a directed edge or increase the weight of one that exists'''
        if dest not in self.nodes[source]:
            self.nodes[source][dest] = 1
            # Check if that generated a two-node cycle
            if source in self.nodes[dest]:
                self.cycles.append((source, dest))
        else:
            # Increment the weight of the edge by 1
            self.nodes[source][dest] += 1


def run_testcase(c, d, votes):
    # Set up the graph
    G = Graph()
    for i in xrange(1, c+1):
        G.add_node('C' + str(i))
    for i in xrange(1, d+1):
        G.add_node('D' + str(i))

    # Add directed edges to the graph based on votes.
    # For example, C1 D1 adds edge C1->D1
    for vote in votes:
        keep, drop = vote.split(' ')
        G.add_edge(keep, drop)

    for cycle in G.cycles:
        # Compute the weights of the outedges of cycle nodes
        sum1 = 0
        sum2 = 0
        for outedge in G.nodes[cycle[0]]:
            sum1 += G.nodes[cycle[0]][outedge]
        for outedge in G.nodes[cycle[1]]:
            sum2 += G.nodes[cycle[1]][outedge]

        # Resolve conflicts
        if sum1 < sum2:
            G.nodes[cycle[0]] = {}
        elif sum1 > sum2:
            G.nodes[cycle[1]] = {}
        else:
            # It's a toss-up; just go with cycle[0]
            G.nodes[cycle[0]] = {}

    # Now that conflicts are resolved, the sum of weights is the answer
    sum_of_weights = 0
    for node in G.nodes.iteritems():
        for _, weight in node[1]: # node[1] is the dict of edge weights
            sum_of_weights += int(weight)

    # Append the result to a list to avoid printing it too early
    global results
    results.append(sum_of_weights)

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
