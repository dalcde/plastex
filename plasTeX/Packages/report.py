#!/usr/bin/env python3

from plasTeX.Packages.book import *
from plasTeX.Packages import book

def ProcessOptions(options, document):
    book.ProcessOptions(options, document)
    document.context['theequation'].format = '${equation}'
