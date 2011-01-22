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
#    BSD license.

__all__ = ['read_shp']

import networkx as nx

def read_shp(path, tolerance=0):
    """Generates a networkx.DiGraph from shapefiles. 

    "The Esri Shapefile or simply a shapefile is a popular geospatial vector
    data format for geographic information systems software [1]_."

    Parameters
    ----------
    path : file or string
       File, directory, or filename to read.
    tolerance : number
        Spatial tolerance of network objects. Nodes within this distance will
        be assumed to be the same.

    Returns
    -------
    G : NetworkX graph

    Examples
    --------
    G=nx.read_shp('test.shp')
    
    References
    ----------
    .. [1] http://en.wikipedia.org/wiki/Shapefile
    """
    try:
        from osgeo import ogr
    except ImportError:
        raise ImportError("read_shp() requires OGR: http://www.gdal.org/")
    
    net = nx.DiGraph()
    
    def getfieldinfo(lyr, feature, flds):
            f = feature
            return [f.GetField(f.GetFieldIndex(x)) for x in flds]
            
    def addlyr(lyr, fields):
        for findex in xrange(lyr.GetFeatureCount()):
            f = lyr.GetFeature(findex)
            flddata = getfieldinfo(lyr, f, fields)
            g = f.geometry()
            attributes = dict(zip(fields, flddata))
            attributes["ShpName"] = lyr.GetName()
            if g.GetGeometryType() == 1: #point
                net.add_node((g.GetPoint_2D(0)), attributes)
            if g.GetGeometryType() == 2: #linestring
                last = g.GetPointCount() - 1
                net.add_edge(g.GetPoint_2D(0), g.GetPoint_2D(last), attributes)
                
    if isinstance(path, str):
        shp = ogr.Open(path)
        lyrcount = shp.GetLayerCount() #multiple layers indicate a directory
        for lyrindex in xrange(lyrcount):
            lyr = shp.GetLayerByIndex(lyrindex)
            flds = [x.GetName() for x in lyr.schema]
            addlyr(lyr, flds)
    return net
    
# fixture for nose tests
def setup_module(module):
    from nose import SkipTest
    try:
        import ogr
    except:
        raise SkipTest("OGR not available")

