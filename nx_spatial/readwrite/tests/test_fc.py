"""
    Unit tests for shp.
"""
 
import os,tempfile,shutil
from nose import SkipTest
from nose.tools import assert_equal

from nx_spatial import read_fc
import networkx as nx

def buildtestnet():
    di = nx.DiGraph()
    di.add_path([(7.0, 1.0), (1.0, 1.0), (2.0, 2.0), (3.0, 3.0)])
    di.add_path([(4.0, 1.0), (2.0, 2.0)])
    di.add_path([(5.0, 5.0), (6.0, 6.0)])
    di.add_path([(6.0, 3.0), (7.0, 7.0)])
    return di

class TestFc(object):
    @classmethod
    def setupClass(cls):
        global gp
        try:
            import arcgisscripting as arc
            gp = arc.create(9.3)
        except ImportError:
            raise SkipTest('ESRI geoprocessor not available.')
            
    def setUp(self):
        gdbname = "tempgdb"
        gdbpath = os.path.join(tempfile.gettempdir(), gdbname)
        gp.CreateFileGDB_management(tempfile.gettempdir(), gdbname)
        gp.CreateFeatureclass_management(gdbpath, "lines")
        self.testfc = os.path.join(gdbpath, "lines")
        self.paths = (  [(1.0, 1.0), (2.0, 2.0)],
                        [(2.0, 2.0), (3.0, 3.0)],
                        [(0.9, 0.9), (4.0, 2.0)]
                    )
        di = nx.DiGraph()
        rows = gp.InsertCursor(os.path.join(gdbpath, "lines"))
        for path in self.paths:
            row = rows.newRow()
            di.add_path(path)
            lineArray = gp.CreateObject("Array")
            for xy in path:
                pnt = gp.CreateObject("Point")
                lineArray.add(xy)
            row.Shape = lineArray
            rows.InsertRow(row)
        self.lines = di.edges()
        self.nodes = di.nodes()
        
    def testload_fcnodes(self):
        G = read_fc(self.testfc, gp)
        assert self.sequence_equal(self.nodes, G.nodes())
        assert self.sequence_equal(self.lines, G.edges())
        
    def sequence_equal(self, seq1, seq2, msg=None):
        msg = str(seq1) + "!=" + str(seq2)
        seq1.sort()
        seq2.sort()
        return seq1 == seq2
                    
if __name__ == '__main__':
    unittest.main()
