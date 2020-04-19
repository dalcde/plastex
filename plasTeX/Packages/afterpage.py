#!/usr/bin/env python3

from plasTeX import Command

class afterpage(Command):
    args = 'self:nox'

    def invoke(self, tex):
        super(afterpage, self).invoke(tex)
        return []
