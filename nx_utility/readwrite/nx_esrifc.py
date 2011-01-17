"""
*********
Shapefile
*********

Generates a networkx.DiGraph from point and line feature classes.

Point geometries are translated into nodes, lines into edges. Coordinate tuples
are used as keys. Attributes are preserved, line geometries are simplified into
start and end coordinates. Accepts a single feature class.

"The Esri Shapefile or simply a shapefile is a popular geospatial vector
data format for geographic information systems software. It is developed
and regulated by Esri as a (mostly) open specification for data
interoperability among Esri and other software products."
See http://en.wikipedia.org/wiki/Shapefile for additional information.

"""
__author__ = """Ben Reilly (benwreilly@gmail.com)"""
#    Copyright (C) 2004-2010 by
#    Ben Reilly <benwreilly@gmail.com>
#    All rights reserved.
#    GPLv2 license.

__all__ = ['read_fc']

import networkx as nx
import nx_utility as nu

def read_fc(path, gp):
    """Generates a networkx.DiGraph from a feature class. 

    "The ESRI Feature Class is a popular geospatial vector
    data format for geographic information systems software."

    Parameters
    ----------
    path : file or string
       File, directory, or filename to read.

    Returns
    -------
    G : NetworkX graph

    Examples
    --------
    G=nu.read_fc('C:\database.gdb\test')

    """    
    net = nx.DiGraph()
    
    def get_attribs(fields):
            fvals = []
            for field in fields:
                if field != "Shape":
                    fvals.append(row.GetValue(field))
            return dict(zip(fields, fvals))
            
    cur = gp.SearchCursor(path)
    fields = map(lambda x: x.name, gp.listfields(path))
    row = cur.Next()
    while row:
        geom = row.GetValue("Shape")
        attributes = get_attribs(fields)
        attributes["FcName"] = path.split("\\")[-1]
        if geom.Type == "point":
            pnt = geom.GetPart(0)
            net.add_node((pnt.x, pnt.y), attributes)
        elif geom.Type == "polyline":
            first = geom.FirstPoint
            last = geom.LastPoint
            net.add_edge((first.x, first.y), (last.x, last.y), attributes)
        row = cur.Next()
    
    return net
    
# fixture for nose tests
def setup_module(module):
    from nose import SkipTest
    try:
        import arcgisscripting
    except:
        raise SkipTest("arcgisscripting not available")
