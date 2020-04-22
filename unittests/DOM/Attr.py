#!/usr/bin/env python3

import unittest
from unittest import TestCase
from plasTeX.DOM import *

class AttributeTest(TestCase):

    def testNodeName(self):
        doc = Document()
        one = doc.createAttribute('one')
        assert one.nodeName == 'one'

    def testNodeValue(self):
        doc = Document()
        one = doc.createAttribute('one')
        assert one.nodeValue is None


if __name__ == '__main__':
    unittest.main()

