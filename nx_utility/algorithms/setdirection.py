from trace import *
from flow_errors import *

def setdirection(G, *sources):
        """Given a set of source nodes, resolve network direction. First in,
        first resolved.
        Usage:
        >>> setdirection(G, (2, 2), (3, 4))
        """
        def repair_edge(badedge):
            e = badedge
            data = G.get_edge_data(*e)
            v,u = e[0], e[1]
            return u,v,data
        
        def flip(edge):
            G.add_edge(*repair_edge(edge))
            G.remove_edge(*edge)
            
        for src in sources:
            errs = flow_errors(src)
            while errs:
                e = errs.pop()
                if e in G.edges():
                    flip(e)
                errs += filter(lambda x: x not in errs, flow_errors(src))