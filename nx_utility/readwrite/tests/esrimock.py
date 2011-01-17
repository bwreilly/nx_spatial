#!/usr/bin/env python
class arcgisscripting(object):
    def create(self, version):
        return GPMock
    
class GPMock(object):
    def __init__(self):
        fcs = []
    def listfeatureclasses(self):
        return fcs
    def SearchCursor(self, fc):
        return SCursorMock()
    def listfields(self, fc):
        return [FieldMock()]
        
class SCursorMock(object):
    def __init__(self, feats=None, ftype=None):
        self.last = 0
        self.features = [RowMock(x, ftype) for x in feats]
    def __iter__(self):
        return self
    def Next(self):
        try:
            x = self.features[self.last]
            self.last += 1
            return x
        except IndexError:
            return None

class RowMock(object):
    def __init__(self, geometry, gtype="Point"):
        self.geom = GeometryMock(geometry, gtype)
    def GetValue(self, fieldname):
        if fieldname == "Shape":
            return self.geom
        else:
            return 1

class FieldMock(object):
    def __init__(self):
        self.name = "fieldname"

class GeometryMock(object):
    def __init__(self, geometry, gtype):
        self.g = geometry
        self.Type = gtype
        if self.Type == "polyline":
            self.FirstPoint = PointMock(self.g[0])
            self.LastPoint = PointMock(self.g[-1])
    def GetPart(self, index):
        return PointMock(self.g)

class PointMock(object):
    def __init__(self, geom):
        self.x = geom[0]
        self.y = geom[1]