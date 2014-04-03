import unittest
import doctest

from zope.component import testing


def test_suite():
    return unittest.TestSuite([

        # Unit tests for your API
        doctest.DocFileSuite(
            'patches.py', package='collective.zexpquickimport',
            setUp=testing.setUp, tearDown=testing.tearDown),

    ])


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
