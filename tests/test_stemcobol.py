#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `stemcobol` package."""

import os
import pytest


from stemcobol import parse, FREE_FORMAT

pwd = os.path.dirname(os.path.realpath(__file__))

srcdir = "%s/cobol/helloworld"%pwd
source = "helloworld.cob"

@pytest.fixture
def srcfile():
    # read source file and convert it to SourceLineTree
    pass

def test_parse():

    tree = parse(os.path.join(srcdir, source), FREE_FORMAT, '')
    node = tree
    while len(node.subnodes) > 0:
        node = node.subnodes[-1]
    assert node.start.text == "STOP" and node.stop.text == "RUN"
