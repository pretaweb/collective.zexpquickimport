from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.zexpquickimport',
      version=version,
      description="Monkey patch zexp import without triggering the object events",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Plone",
      ],
      keywords='',
      author='Ivan Teoh',
      author_email='ivan@pretaweb.com',
      url='https://github.com/collective/collective.zexpquickimport',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'collective.monkeypatcher',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
