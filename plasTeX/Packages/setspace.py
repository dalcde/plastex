#!/usr/bin/env python3

from plasTeX import IgnoreCommand

class doublespacing(IgnoreCommand):
    pass

class singlespacing(IgnoreCommand):
    pass

class onehalfspacing(IgnoreCommand):
    pass

class setstretch(IgnoreCommand):
    args = 'size:nox'
