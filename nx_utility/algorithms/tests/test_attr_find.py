import os,tempfile,shutil
from nose import SkipTest
from nose.tools import assert_equal

import networkx as nx
from nx_utility import attr_find

class TestAttr_Find(object):   
    def setUp(self):
        self.di = nx.DiGraph()
        self.di.add_node((5,15), FcName='test', Id=5)
        self.di.add_node((5,20), FcName='test', Id=6)
        self.di.add_node((5,21), FcName='test', Id=10, Shape='point')
        self.di.add_node((5,40), FcName='test2', Id=5, Shape='point')
        self.di.add_edge((5,15), (5,20), FcName='line', Id=6)
        self.assertEqual = assert_equal
    def testfind_onenode(self):
        net = self.di
        expected = [(5,15)]
        actual = attr_find(net, Id=5, FcName='test')
        self.assertEqual(expected, actual)
    def testfind_multiplenodes(self):
        net = self.di
        expected = [(5,15), (5,40)]
        actual = attr_find(net, Id=5)
        self.assertEqual(expected, actual)
    def testfind_nomatch(self):
        net = self.di
        expected = []
        actual = attr_find(net, Id=7)
        self.assertEqual(expected, actual)
    def testfind_wrongval(self):
        net = self.di
        expected = []
        actual = attr_find(net, FcName='test2', Shape='what')
        self.assertEqual(expected, actual)
    def testfind_wrongattr(self):
        net = self.di
        expected = []
        actual = attr_find(net, FcName='test2', Geom='what', Shape='point')
        self.assertEqual(expected, actual)
    def testfind_givenlist(self):
        net = self.di
        expected = [(5, 21)]
        nodes = [(5, 40), (5, 15), (5, 21)]
        actual = attr_find(net, nodes, FcName='test', Shape='point')
        self.assertEqual(expected, actual)
    def testfind_everything(self):
        net = self.di
        expected = [(5,15), (5,40), (5, 40)].sort()
        actual = attr_find(net).sort()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()