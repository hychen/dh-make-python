#!/usr/bin/env python
# -*- encoding=utf8 -*-
#
# Author 2010 Hsin-Yi Chen
#
# This is a free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# This software is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this software; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA 02111-1307 USA
import unittest
import os

from dh_make_python import metadata
from dh_make_python import template

datadir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'datas')
def tdata_open(path):
    "open test data file"
    path = os.path.join(datadir, path)
    return open(path, 'r')

class MetadataTestCase(unittest.TestCase):

    #{{{def setUp(self):
    def setUp(self):
        self.srcinfo = metadata.SrcInfo(datadir)
        self.debinfo=metadata.DebInfo(self.srcinfo)
        self.debinfo.today822 = 'Wed, 09 Feb 2011 11:26:24 +0800'
        self.debinfo.maintainer_fullname = 'Hsin-Yi Chen (hychen) <ossug.hychen@gmail.com>'
    #}}}

    #{{{def tearDown(self):
    def tearDown(self):
        pass
    #}}}

    #{{{def testLoadInfo(self):
    def testLoadInfo(self):
        _srcinfo = metadata.SrcInfo(datadir)
        _srcinfo.load('PKG-INFO')
        _srcinfo.load('setup.py')
        self.assertEquals(self.srcinfo.author_email, 'ossug.hychen@gmail.com')
        self.assertEquals(self.debinfo.upstream_contact_email, 'ossug.hychen@gmail.com')
    #}}}

    #{{{def test(self):
    def testDebianlize(self):
        t = template.Changelog(self.debinfo)
#        self.assertEquals(tdata_open('changelog').read(), "%s"%t)
        t = template.Control(self.debinfo)
        #print t
        t = template.Copyright(self.debinfo)
        #print t
#        o=template.DebianizeDir(self.debinfo)
#        print o.create()
        #o.save('/tmp/debian')
    #}}}
pass

def suite():
    return unittest.makeSuite(MetadataTestCase, 'test')

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
