from trace import *

def flow_errors(G, src, stopnodes=None):
    """Returns the first edges that do not conform to the flow direction
    implicit in defined source node.
    """
    badedges = []
    gnodes = trace(G, src, stopnodes)
    #ud = self.to_undirected()
    #connected = networkx.dfs_preorder(src)
    for edge in G.edges(): #todo: limit to potentially connected
        start = edge[0]
        end = edge[1]
        if end in gnodes and start not in gnodes:
                badedges.append(G.edges(start)[0])
    return badedges