def attr_find(G, nodes=None, **attributes):
    """Find specific nodes based on given attributes. By default searches
    all network nodes.
    nx.attr_find(G, Id=1, Name='Bob') -> [(6,2)]
    """
    attrib = attributes
    found = []
    if not nodes:
        nds = G.node.iteritems()
    else:
        nodes.sort()
        keys = filter(lambda a: a in nodes, G.node)
        vals = map(lambda x: G.node[x], nodes)
        nds = zip(keys, vals)
    for xy, attr in nds:  # (x, y): {attributes}
        if set(attrib).issubset(attr):  # has all search keys
            if all(map(lambda x: attr[x] == attrib[x], attrib.keys())):
                found.append(xy)
    return list(set(found))
