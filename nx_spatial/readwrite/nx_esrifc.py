"""
*********
Feature Class
*********

Generates a networkx.DiGraph from point and line feature classes.

Point geometries are translated into nodes, lines into edges. Coordinate tuples
are used as keys. Attributes are preserved, line geometries are simplified into
start and end coordinates. Accepts a single feature class.

"""
__author__ = """Ben Reilly (benwreilly@gmail.com)"""
#    Copyright (C) 2004-2010 by
#    Ben Reilly <benwreilly@gmail.com>
#    All rights reserved.
#    GPLv2 license.

__all__ = ['read_fc']

import networkx as nx


def read_fc(workspace, gp):
    """Generates a networkx.DiGraph from a feature class.

    "The ESRI Feature Class is a popular geospatial vector
    data format for geographic information systems software."

    Parameters
    ----------
    workspace : file or string
       ESRI workspace - folder or geodatabase file path
    gp : ESRI geoprocessor object

    Returns
    -------
    G : NetworkX graph

    Examples
    --------
    G=nu.read_fc('C:\database.gdb')

    """
    net = nx.DiGraph()

    def get_attribs(fields):
            attributes = {}
            for field in fields:
                if field != "Shape":
                    attributes[field] = row.GetValue(field)
            return attributes

    gp.workspace = workspace
    for fc in gp.listfeatureclasses():
        cur = gp.SearchCursor(fc)
        fields = map(lambda x: x.name, gp.listfields(fc))
        row = cur.Next()
        while row:
            geom = row.GetValue("Shape")
            attributes = get_attribs(fields)
            attributes["FcName"] = fc
            if geom.Type == "point":
                pnt = geom.GetPart(0)
                net.add_node((pnt.x, pnt.y), attributes)
            elif geom.Type == "polyline":
                first = geom.FirstPoint
                last = geom.LastPoint
                net.add_edge((first.x, first.y), (last.x, last.y), attributes)
            row = cur.Next()
        del cur
    return net


# fixture for nose tests
def setup_module(module):
    from nose import SkipTest
    try:
        import arcgisscripting
    except:
        raise SkipTest("arcgisscripting not available")
