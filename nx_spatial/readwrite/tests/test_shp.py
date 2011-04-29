"""
    Unit tests for shp.
"""
 
import os,tempfile
from nose import SkipTest
from nose.tools import assert_equal

import networkx as nx
import nx_spatial as nu

class TestShp(object):
    @classmethod
    def setupClass(cls):
        global ogr
        try:
            from osgeo import ogr
        except ImportError:
            raise SkipTest('ogr not available.')
            
    def setUp(self):
        drv = ogr.GetDriverByName("ESRI Shapefile")
        testdir = os.path.join(tempfile.gettempdir(),'shpdir')
        os.mkdir(testdir)
        shppath = os.path.join(tempfile.gettempdir(),'tmpshp.shp')
        if os.path.exists(shppath): drv.DeleteDataSource(shppath)      
        shp = drv.CreateDataSource(shppath)
        lyr = shp.CreateLayer("edges", None, ogr.wkbLineString)
        
        self.paths = (  [(1.0, 1.0), (2.0, 2.0)],
                        [(2.0, 2.0), (3.0, 3.0)],
                        [(0.9, 0.9), (4.0, 2.0)]
                    )
        for path in self.paths:
            feat = ogr.Feature(lyr.GetLayerDefn())
            g = ogr.Geometry(ogr.wkbLineString)
            map(lambda xy: g.AddPoint_2D(*xy), path)
            feat.SetGeometry(g)
            lyr.CreateFeature(feat)
        self.shppath = shppath
        self.testdir = testdir
        self.drv = drv
        self.G = None

    def testload(self):
        expected = nx.DiGraph()
        map(expected.add_path, self.paths)
        G = nu.read_shp(self.shppath)
        assert_equal(sorted(expected.node), sorted(G.node))
        assert_equal(sorted(expected.edges()), sorted(G.edges()))
    
    def testexport(self):
        expectednodes = (
            ogr.Geometry(type=ogr.wkbPoint, wkt="POINT(1 1)"),
            ogr.Geometry(type=ogr.wkbPoint, wkt="POINT(2 2)"),
            ogr.Geometry(type=ogr.wkbPoint, wkt="POINT(3 3)"),
            ogr.Geometry(type=ogr.wkbPoint, wkt="POINT(0.9 0.9)"),
            ogr.Geometry(type=ogr.wkbPoint, wkt="POINT(4 2)")
        )
        tpath = os.path.join(tempfile.gettempdir(),'shpdir')
        nu.write_shp(self.G, tpath)
        shpdir = ogr.Open(tpath)
        nodes = shpdir.GetLayerByName("nodes")
        

    def tearDown(self):
        self.drv.DeleteDataSource(self.shppath)
        self.drv.DeleteDataSource(self.testdir)
        
if __name__ == '__main__':
    import unittest
    unittest.main()