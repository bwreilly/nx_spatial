from setuptools import setup, find_packages
import sys, os

version = '0.5'

setup(name='nx_spatial',
      version=version,
      description="Additional GIS focused functions for networkx graphs.",
      long_description="""\
        This project is designed as an add-on for networkx, a graph library for
      Python. It accepts a variety of different spatial formats to generate
      directional graphs and provides simple modules to correct flow errors,
      find specific nodes by attribute, and run a depth first search (trace)
      with stopping points.
""",
      classifiers=['Topic :: Scientific/Engineering :: GIS'], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='spatial, gis, topology, networkx',
      author='Ben Reilly',
      author_email='gallipoli@gmail.com',
      url='http://bitbucket.org/gallipoli/nx_spatial',
      license='MPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      setup_requires=['networkx>=1.2'],
      install_requires=[
          'networkx>=1.2'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
