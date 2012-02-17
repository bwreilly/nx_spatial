def trace(G, source, stopnodes=None, upstream=False):
    """Returns nodes upstream or downstream of given source,
    halting at given list of stop nodes.
    """
    #this code is a modification of the existing networkx.dfs_preorder
    #algorithm, see https://networkx.lanl.gov/
    reverse_graph = upstream
    if source is None:
        nlist = G.nodes()  # process entire graph
    else:
        nlist = [source]  # only process component with source

    if reverse_graph:
        try:
            neighbors = G.predecessors_iter
        except:
            neighbors = G.neighbors_iter
    else:
        neighbors = G.neighbors_iter

    pre = []  # list of nodes in a DFS preorder
    seen = {}  # nodes seen, halt at these
    if stopnodes:
        for stop in stopnodes:
            pre.append(stop)
            seen[stop] = True
    for source in nlist:
        if source in seen:
            continue
        queue = [source]     # use as LIFO queue
        while queue:
            v = queue[-1]
            if v not in seen:
                pre.append(v)
                seen[v] = True
            done = 1
            for w in neighbors(v):
                if w not in seen:
                    queue.append(w)
                    done = 0
                    break
            if done == 1:
                queue.pop()
    return pre
