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
import shutil

from dh_make_python import downloader
from dh_make_python import util
from dh_make_python import metadata

class MetadataTestCase(unittest.TestCase):

    #{{{def setUp(self):
    def setUp(self):
        self.tmpdir = '/tmp/dhmake'
        os.mkdir(self.tmpdir)
        self.pypi = downloader.PyPI()
    #}}}

    #{{{def tearDown(self):
    def tearDown(self):
        shutil.rmtree(self.tmpdir)
    #}}}

    def testDownloadAndUnpack(self):
        url = self.pypi.getDownloadUrl('setuptools')
        tmppath = self.pypi.download(*url)
        util.unpack_tgz(tmppath, self.tmpdir)
        self.assertEquals(metadata.SrcInfo(self.tmpdir).name, 'setuptools')

pass

def suite():
    return unittest.makeSuite(MetadataTestCase, 'test')

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
