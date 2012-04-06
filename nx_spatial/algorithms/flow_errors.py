from trace import *
from networkx import dfs_tree


def flow_errors(G, src, ud=None, stopnodes=None):
    """Returns the first edges that do not conform to the flow direction
    implicit in defined source node.
    G: target digraph
    src: source nodes
    ud: undirected graph (faster iteration with setdirection)
    stopnodes: break points in the network
    """
    if not ud:
        ud = G.to_undirected()
    badedges = []
    gnodes = trace(G, src, stopnodes)
    connected = G.edges(dfs_tree(ud, src).nodes())
    for edge in connected:
        start = edge[0]
        end = edge[1]
        if end in gnodes and start not in gnodes:
                badedges.append(G.edges(start)[0])
    return badedges
