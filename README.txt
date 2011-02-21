# vim:syn=rst:
========================================
dh-make-python
========================================
To use git to manage debian package upstream and debian dir

# creat a tmeplate of debianlize source in debian_branch (unstable default)

dh_make_python get - get source and unpack to current direcotry
dh_make_python import - import source to git repo
dh_make_python debianlize - create debian/ from metadata of python lib
dh_make_python start - do debianlize of python lib

please read help for more detail:

user@hsot# dh_make_python -h

Depends
=======

Install python-ucltip

Ubuntu Maverick

::

        user@host# add-apt-repository ppa:ossug-hychen/python-ucltip
        user@host# apt-get install python-ucltip

Installation
============

[note] this is still in develop! please try it without installation

::
        user@host# git clone git://github.com/hychen/dh-make-python.git
        # setup up enviroment
        user@host# export PYTHONPATH=$PWD/dh-make-python:$PYTHONPATH
        user@host# alias dh_make_python=$PWD/dh-make-python/bin/dh_make_python
        # now you can use it
        # dh_make_python -h

Example of creating a new debian package:
=======================================

::
        # download last release source from pypi and unpack to current directory
        user@host# dh_make_python start ucltip --pypi
        # correct debian/*
        user@host# vi debian/*
        # build and test package...
        user@host# debuild
        # import new source to debian branch of git,
        # the following command will teach you how to do this
        user@hsot# dh_make_python import
