import os
import re

from dh_make_python import util

class SrcInfo(object):

    """
    Source Information
    """

    #{{{def __init__(self, fd):
    def __init__(self, fd):
        """Init

        @param File fd File Description
        """
        self.load(fd)
    #}}}

    #{{{def load(self, fd):
    def load(self, fd):
        """
        load metadata from file

        @param File fd File Description
        """
        self.__dict__.update(self.parse(fd))
    #}}}

    #{{{def parse(self, fd):
    def parse(self, fd):
        """
        parse metadata from file

        @param File fd
        @return dict
        """
        class _Catcher():
            self.data = {}
            def __call__(self, **kargs):
                self.data = kargs
        setup = _Catcher()
        r= re.findall('setup(.*)', fd.read(), re.DOTALL)
        try:
            eval(r[0])
            ret = setup.data
            del(_Catcher)
            del(setup)
            return ret
        except:
            return None
    #}}}

    #{{{def author_full(self):
    @property
    def author_full(self):
        return util.contact_fullname(self.author, self.author_email)
    #}}}
pass

class DebInfo(object):

    upstream_prefix = 'upstream'

    def __init__(self, srcinfo):
        self.srcinfo = srcinfo
        self.today822 = ucltip.get_today822()

    #{{{def __getattr__(self, k):
    def __getattr__(self, k):
        if k.startswith(self.upstream_prefix):
            try:
                return getattr(self.srcinfo,
                               srcinfo_name(k[1+len(self.upstream_prefix):]))
            except AttributeError:
                pass
    #}}}
pass

#{{{def srcinfo_name(k):
def srcinfo_name(k):
    """transform to SrcInfo attribute name"""
    return k.replace('contact', 'author')
#}}}

class SrcInfo(object):

    """
    Source Information
    """

    #{{{def __init__(self, srcdir=None):
    def __init__(self, srcdir=None):
        """Init

        @param File fd File Description
        """
        self.srcdir=srcdir
        try:
            self.load('setup.py')
        except ValueError:
            # parse PKG-INFO, but get very few metadata
            self.load('PKG-INFO')
    #}}}

    #{{{def load(self, fname):
    def load(self, fname):
        """
        load metadata from file

        @param File fd File Description
        """
        with open(os.path.join(self.srcdir, fname)) as fd:
            if os.path.basename(fd.name) == 'setup.py':
                self.parseSetup(fd)
            else:
                self.parsePkgInfo(fd)
    #}}}

    def parseSetup(self, fd):
        class _Catcher():
            self.data = {}
            def __call__(self, **kargs):
                self.data = kargs
        setup = _Catcher()
        r= re.findall('\n(setup.*)\n', fd.read(), re.DOTALL)
        try:
            eval(r[0].strip())
            self.__dict__.update(setup.data)
            del(_Catcher)
            del(setup)
        except Exception, e:
            raise ValueError("Can not parse %s"%fd.name)

    def parsePkgInfo(self, fd):
        from debian import deb822
        data = deb822.Deb822(fd)
        self.name = data.get('Name')
        self.author = data.get('Author')
        self.author_email = data.get('Author-email')
        self.url = data.get('Home-Page')
        self.description = data.get('Summary')
        self.long_description = data.get('Description')
        self.version = data.get('Version')
        self.license = data.get('License')

    #{{{def author_fullname(self):
    @property
    def author_fullname(self):
        return util.contact_fullname(self.author, self.author_email)
    #}}}
pass

class DebInfo(object):

    upstream_prefix = 'upstream'

    #{{{def __init__(self, srcinfo):
    def __init__(self, srcinfo):
        self.srcinfo = srcinfo
        self.load()
    #}}}

    #{{{def load(self):
    def load(self):
        """
        load metadatas from SrcInfo
        """
        self.today822 = util.get_today822()

        # contact information
        self.upstream_name = self.srcinfo.name
        self.upstream_version = self.srcinfo.version
        self.upstream_license = self.srcinfo.license
        self.upstream_contact = self.srcinfo.author
        self.upstream_contact_email = self.srcinfo.author_email
        self.upstream_contact_fullname = self.srcinfo.author_fullname
        self.maintainer = os.getenv('DEBEFULLNAME') or self.upstream_contact
        self.maintainer_email = os.getenv('DEBEMAIL') or self.upstream_contact_email
        self.maintainer_fullname = util.contact_fullname(self.maintainer, self.maintainer_email)

        # deb package information
        self.homepage = self.srcinfo.url
        self.debname = util.pydebianize_name(self.srcinfo.name)
        self.debver = self.srcinfo.version+'-1'
        self.source = self.debname
        self.uploaders = ''
        self.debian_section = 'python'
        self.architecture = 'all'
        self.build_depends = 'python-support (>= 0.90), debhelper (>= 7)'
        self.package_stanza_extras = ''
        self.source_stanza_extras = ''
        self.depends = '${python:Depends}, ${misc:Depends}'
        self.description = self.srcinfo.description
        self.long_description = self._fmt_longdesc(self.srcinfo.long_description)
    #}}}

    #{{{def _fmt_longdesc(self, longdesc):
    def _fmt_longdesc(self, longdesc):
        return '\n'.join([' '+line for line in longdesc.split('\n') if line])
    #}}}
pass
