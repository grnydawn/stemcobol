#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `stemcobol` package."""

import os
import pytest


from stemcobol import parse, FIXED_FORMAT

pwd = os.path.dirname(os.path.realpath(__file__))

srcdir = "%s/cobol/senior"%pwd
source = "senior.cob"

@pytest.fixture
def srcfile():
    # read source file and convert it to SourceLineTree
    pass

def test_parse():

    # read source file
    with open(os.path.join(srcdir, source)) as f:
        tree = parse(f.read(), FIXED_FORMAT, '')
        node = tree
        while len(node.subnodes) > 0:
            node = node.subnodes[-1]
        assert node.start.text == "PRINT-LINE"
