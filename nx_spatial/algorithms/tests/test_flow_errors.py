from nose.tools import assert_equal

import networkx as nx
from nx_spatial import flow_errors


class TestFlow_Errors(object):
    def setUp(self):
        self.di = nx.DiGraph()
        self.di.add_path([(7.0, 1.0), (1.0, 1.0), (2.0, 2.0), (3.0, 3.0)])
        self.di.add_path([(4.0, 1.0), (2.0, 2.0)])
        self.di.add_path([(5.0, 5.0), (6.0, 6.0)])
        self.di.add_path([(6.0, 3.0), (7.0, 7.0)])
        self.assertEqual = assert_equal

    def testflow_errors_oneedgegroup(self):
        src = ((1, 1))
        badline1 = ((4, 1), (2, 2))
        badline2 = ((7, 1), (1, 1))
        expected = [badline1, badline2]
        actual = flow_errors(self.di, src)
        assert self.sequence_equal(actual, expected)

    def testflow_errors_twoedgegroup(self):
        src = ((2.0, 2.0))
        badline1 = ((4, 1), (2, 2))
        badline2 = ((1, 1), (2, 2))
        expected = [badline1, badline2]
        actual = flow_errors(self.di, src)
        assert self.sequence_equal(actual, expected)

    def testflow_errors_single_edge(self):
        src = ((7.0, 7.0))
        badline1 = ((6, 3), (7, 7))
        expected = [badline1]
        actual = flow_errors(self.di, src)
        assert self.sequence_equal(actual, expected)

    def sequence_equal(self, seq1, seq2, msg=None):
        seq1.sort()
        seq2.sort()
        return seq1 == seq2
