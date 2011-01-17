from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='nx_spatial',
      version=version,
      description="Additional GIS focused functions for networkx graphs.",
      long_description="""\
                       
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='spatial, gis, topology, networkx',
      author='Ben Reilly',
      author_email='gallipoli@gmail.com',
      url='http://bitbucket.org/gallipoli/nx_spatial',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      setup_requires=['networkx>=1.0'],
      install_requires=[
          'networkx>=1.0'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
