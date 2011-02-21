# find source code url in pypi
# download source code from download url to temp dir
# unpack source code to current dir
#
# pypi
import os
import xmlrpclib
import urllib2
import tempfile
import hashlib

class PyPI(object):

    def __init__(self):
        self.transport = xmlrpclib.Transport()
        self.rpc = xmlrpclib.ServerProxy('http://python.org/pypi', transport=self.transport)

    def getDownloadUrl(self, pkgname, want_ver=None):
        releases = self.rpc.package_releases(pkgname)
        for version in releases:
            urls = self.rpc.release_urls(pkgname, version)
            for url in urls:
                if url['url'].endswith('.tar.gz'):
                    try:
                        return url['url'], url['md5_digest']
                    except KeyError:
                        return url['url'], None

    def download(self, download_url, expected_md5=None):
        """download .tar.gz from url in /tmp

        @param url .tar.gz url
        @param except_md5, except_md5
        @return str temp file path
        """
        request = urllib2.Request(download_url)
        opener = urllib2.build_opener()
        package_tar_gz = opener.open(request).read()
        if expected_md5:
            m = hashlib.md5()
            m.update(package_tar_gz)
            actual_md5_digest = m.hexdigest()
            if actual_md5_digest != expected_md5:
                raise ValueError('actual and expected md5 digests do not match')
        fname = os.path.join(tempfile.gettempdir(), download_url.split('/')[-1])
        with open(fname,mode='wb') as fd:
            fd.write(package_tar_gz)
        return fname
