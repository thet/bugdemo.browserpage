import unittest
import doctest

from Products.Five import zcml
from Products.Five import fiveconfigure

from Testing import ZopeTestCase as ztc
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

from interlude import interact

@onsetup
def setup_bugdemo_browserpage():
    fiveconfigure.debug_mode = True
    import bugdemo.browserpage
    zcml.load_config('configure.zcml', bugdemo.browserpage)
    fiveconfigure.debug_mode = False
    ztc.installPackage('bugdemo.browserpage')

setup_bugdemo_browserpage()
ptc.setupPloneSite(products=['bugdemo.browserpage'])

OPTION_FLAGS = doctest.REPORT_ONLY_FIRST_FAILURE | \
            doctest.NORMALIZE_WHITESPACE | \
            doctest.ELLIPSIS

def test_suite():

    suite = ztc.ZopeDocFileSuite(
            'README.txt',
            package='bugdemo.browserpage',
            test_class=ptc.FunctionalTestCase,
            optionflags=OPTION_FLAGS,
            globs={'interact': interact,},
    )
    return unittest.TestSuite([suite,])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
