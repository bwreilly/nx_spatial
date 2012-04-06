"""
*********
Shapefile
*********

Generates a networkx.DiGraph from point and line shapefiles.

Point geometries are translated into nodes, lines into edges. Coordinate tuples
are used as keys. Attributes are preserved, line geometries are simplified into
start and end coordinates. Accepts a single shapefile or directory of many
shapefiles.

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

__all__ = ['read_shp', 'write_shp']

import networkx as nx


def read_shp(path):
    """ Active development for shp read is now done in networkx. This function left in for compatibilty purposes.
    """
    return nx.read_shp(path)


def write_shp(G, outdir):
    """ Active development for shp write is now done in networkx. This function left in for compatibilty purposes.
    """
    nx.write_shp(G, outdir)


# fixture for nose tests
def setup_module(module):
    from nose import SkipTest
    try:
        import ogr
    except:
        raise SkipTest("OGR not available")

