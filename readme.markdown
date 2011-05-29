# Spatial/GIS oriented extensions for the networkx graph library. Requires networkx.


### Usage
	>>> import nx_spatial as ns
	>>> net = ns.read_shp('/shapes/lines.shp')     ### import from shapefile
	>>> net.edges()
	[[(1.0, 1.0), (2.0, 2.0)], [(2.0, 2.0), (3.0, 3.0)], [(0.9, 0.9), (4.0, 2.0)]]
	>>> net.nodes()
	[(1.0, 1.0), (2.0, 2.0), (3.0, 3.0), (0.9, 0.9), (4.0, 2.0)]
	>>> source = (2.0, 2.0)
	>>> ns.setdirection(net, source)               ### reset network direction 		based on source
	>>> net.edges()
	[[(2.0, 2.0), (1.0, 1.0)], [(2.0, 2.0), (3.0, 3.0)], [(0.9, 0.9), (4.0, 2.0)]]
	>>> ns.write_shp(net, '~\shapefiles')          ### export to shapefiles

### Installation
	$ hg clone http://bitbucket.org/gallipoli/nx_utility/
	$ python setup.py install

OR
	$ easy_install nx_spatial

OR
	$ pip install nx_spatial

### Development Status
API relatively stable.

Developed on Ubuntu. Tested working on WinXP, Win7.