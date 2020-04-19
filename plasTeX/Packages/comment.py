#!/usr/bin/env python3

from plasTeX.Base.LaTeX.Verbatim import verbatim

class comment(verbatim):

    def invoke(self, tex):
        verbatim.invoke(self, tex)
        return []
