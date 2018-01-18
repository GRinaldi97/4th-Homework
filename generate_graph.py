#We solved the problem by creating a graph from the dictionary.
#A graph is a structure made of nodes which are connected by edges

#We created our graph using networkx
#In our graph the nodes are all the words of the dictionary, and two nodes are connected with an edge if they differ by just one letter (insertion, deletions and substitutions are allowed)

#After creating the graph we used the function shortest_path to find out if it was possible to transform a word into another through a serie of valid itermediates

#The process of creating a graph is what tends to slow down the program because we had to iterate over all the words of the dictionary (which contains over 479k words)
#However after creating the graph it can be used it multiple time to search a path between two words

#Moreover we used the same graph both for the first and for the second problem (generalized equivalent words)
#That is because generalizing the graph required just one more line of code and it was not time consuming
#Moreover we've used a very useful tool of NetWorkx that is 'pickle' that allows us to save the graph generated (that is uploaded)


from string import ascii_lowercase as lowercase
import networkx as nx

file = open('words_alpha.txt', 'r')
dictionary = set([word for word in file.read().split()])


def generate_graph(words):

    G = nx.Graph()
    letters_index = dict((c, lowercase.index(c)) for c in lowercase)
    G.add_nodes_from(words)

    def transformations(word):
        for i in range(len(word)):
            left = word[0:i]
            c = word[i]
            right = word[i + 1:]

            yield left + right      #deletion. This line generalize the problem. There's no need to write something also for insertion since the graph is unidirected.
                                                                                #So insertion in covered when we perform deletion in words that are one letter longer
            j = letters_index[c]        #the index of the letter in the alphabeth, we can transform the word starting from that letter to save time. The transformations with the letters that are alpabethically smaller has already been done with previous words
            for cc in lowercase[j + 1:]:
                yield left + cc + right     #substitution

    for word in words:
        candgen = ((word, candidate) for candidate in transformations(word) if candidate in words)
        for word, candidate in candgen:
            G.add_edge(word, candidate)

    return G

G = generate_graph(dictionary)
nx.write_gpickle(G,"GeneratedGraph")
