import ucltip
import os
import tempfile
import subprocess
import shutil

def unpack_tgz(tgzpath, dest):
    dname = tgzpath.split('/')[-1].replace('.tar.gz','')
    tmpdir = tempfile.mkdtemp()
    subprocess.call(['tar','xzvf', tgzpath, '-C', tmpdir])
    subprocess.call('mv %s/* %s'%(os.path.join(tmpdir,dname), dest), shell=True)
    shutil.rmtree(tmpdir)

#{{{def contact_fullname(name, email):
def contact_fullname(name, email):
    return "%s <%s>" % (name, email)
#}}}

#{{{def get_today822():
def get_today822():
    """return output of 822-date command"""
    try:
        return ucltip.SingleCmd('date')(R=True).strip().replace('\n','')
    except ucltip.CommandNotFound:
        return None
#}}}

def debian_branch_name(dist):
    return "%s_%s"%(dist[0].lower(),dist[2].lower())

def pydebianize_name(name):
    return 'python-'+debianize_name(name)

def debianize_name(name):
    "make name acceptable as a Debian (binary) package name"
    name = name.replace('_','')
    name = name.lower()
    return name

def source_debianize_name(name):
    "make name acceptable as a Debian source package name"
    name = name.replace('_','')
    name = name.replace('.','-')
    name = name.lower()
    return name

def debianize_version(name):
    "make name acceptable as a Debian package name"
    name = name.replace('_','-')

    # XXX should use setuptools' version sorting and do this properly:
    name = name.replace('.dev','~dev')

    name = name.lower()
    return name
