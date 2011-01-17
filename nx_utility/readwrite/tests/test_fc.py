"""
    Unit tests for shp.
"""
 
import os,tempfile,shutil
from nose import SkipTest
from nose.tools import assert_equal

from nx_utility import read_fc
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
            raise SkipTest('gp mock not available.')
            
    def setUp(self):
        di = buildtestnet()
        self.lines = di.edges()
        self.nodes = di.nodes()
        
    def testload_fcnodes(self):
        G = read_fc("C:\\somefakedb.mdb\\fakenodes", gp)
        assert self.sequence_equal(self.nodes, G.nodes())
        
    def testload_fcedges(self):
        G = read_fc("C:\\somefakedb.mdb\\fakenodes", gp)
        assert self.sequence_equal(self.lines, G.edges())
        
    def sequence_equal(self, seq1, seq2, msg=None):
        msg = str(seq1) + "!=" + str(seq2)
        seq1.sort()
        seq2.sort()
        return seq1 == seq2
                    
if __name__ == '__main__':
    unittest.main()
