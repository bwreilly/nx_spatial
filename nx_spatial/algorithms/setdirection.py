from trace import *
from flow_errors import *


def setdirection(G, stopnodes=None, *sources):
        """Given a set of source nodes, resolve network direction. First in,
        first resolved.
        Usage:
        >>> setdirection(G, (2, 2), (3, 4))
        """
        ud = G.to_undirected()

        def repair_edge(badedge):
            e = badedge
            data = G.get_edge_data(*e)
            v, u = e[0], e[1]
            return u, v, data

        def flip(edge):
            G.add_edge(*repair_edge(edge))
            G.remove_edge(*edge)

        for src in sources:
            errs = set(flow_errors(G, src, ud, stopnodes))
            while errs:
                e = errs.pop()
                flip(e)
                errs.union(set(flow_errors(G, ud, src, stopnodes)))
