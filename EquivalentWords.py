from generate_graph import generate_graph
from string import ascii_lowercase as lowercase
import networkx as nx

file = open('words_alpha.txt', 'r')
dictionary = set([word for word in file.read().split()])

G = generate_graph(dictionary)
source = 'head'
target = 'tail'

print('Graph generated from the file words_alpha.txt containing 479k English words.')
print('The graph has' + str(nx.number_of_nodes(G))+ ' connected with ' + str(nx.number_of_edges(G)))
print(str(nx.number_connected_components(G)) + 'connected components')
print('Two words are connected if they differ in one letter. Insertions, deletions, and substitutions are allowed.')
print('')

print('The shortest path between ' + source + ' and ' + target +' is:')
try:
    sp = nx.shortest_path(G, source, target)
    print(' ---> '.join(sp))
except nx.NetworkXNoPath:
    print("None")
print ('')


#We can also use a list of words:
#If no path exist like in the case of 'structure' and 'context' the program will rise an exception and return None

List = [('head', 'tail'),('head', 'tea'),('tampering', 'crunchier'),('cake', 'limp'),('structure','context'),('pound', 'marks')]
for (source, target) in List:
    print('The shortest path between ' + source + ' and ' + target +' is:')
    try:
        sp = nx.shortest_path(G, source, target)
        print(' ---> '.join(sp))
    except nx.NetworkXNoPath:
        print('None')
    print('')