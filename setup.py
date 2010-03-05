from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='bugdemo.browserpage',
      version=version,
      description="",
      long_description=open("README.txt").read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Johannes Raggam',
      author_email='raggam-nl@adm.at',
      url='http://github.com/thet/bugdemo.browserpage',
      license='GPL',
      packages = find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['bugdemo'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      extras_require = dict(
          test = ['interlude',],
      ),
      )
