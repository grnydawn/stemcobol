# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

"""Main module."""

import re
from collections import OrderedDict, MutableMapping
from io import StringIO

from antlr4 import (InputStream, CommonTokenStream, ParseTreeWalker,
    BufferedTokenStream, ParserRuleContext, TerminalNode)

from .parser.Cobol85Lexer import Cobol85Lexer
from .parser.Cobol85Listener import Cobol85Listener
from .parser.Cobol85Parser import Cobol85Parser

from stemtree import Node, SourceLines

# COMMENT ENTRIES

#   REMARKS DOT_FS commentEntry? END_REMARKS? DOT_FS?
#   SECURITY DOT_FS commentEntry?
#   DATE_COMPILED DOT_FS commentEntry?
#   DATE_WRITTEN DOT_FS commentEntry?
#   INSTALLATION DOT_FS commentEntry?
#   AUTHOR DOT_FS commentEntry?
#   PROGRAM_ID DOT_FS programName (IS? (COMMON | INITIAL | LIBRARY | DEFINITION | RECURSIVE) PROGRAM?)? DOT_FS? commentEntry?
_re_remarks = re.compile(r'\s*remarks\s*\.?(?P<cmtentry>\s+[^\s]*)', re.I)
_re_security = re.compile(r'\s*security\s*\.?(?P<cmtentry>\s+[^\s]*)', re.I)
_re_date_compiled = re.compile(r'\s*date-compiled\s*\.?(?P<cmtentry>\s+[^\s]*)', re.I)
_re_date_written = re.compile(r'\s*date-written\s*\.?(?P<cmtentry>\s+[^\s]*)', re.I)
_re_installation = re.compile(r'\s*installation\s*\.?(?P<cmtentry>\s+[^\s]*)', re.I)
_re_author = re.compile(r'\s*author\s*\.?(?P<cmtentry>\s+[^\s]*)', re.I)
_re_program_id = re.compile(r'\s*program-id\s*\.?\s+[_a-z][0-9_a-z\-]*((\s+is)?\s+(common|initial|library|definition|recursive)(\s+program)?)?\s*\.?(?P<cmtentry>.*)', re.I)

cmtentry_patterns = (_re_remarks, _re_security, _re_date_compiled,
    _re_date_written, _re_installation, _re_author, _re_program_id
)

FIXED_FORMAT, FREE_FORMAT, VARIABLE_FORMAT = range(3)


def tocobol_proxy(obj):

    if hasattr(obj, 'text'):
        return obj.text
    else:
        return ''.join([c.tocobol() for c in obj.subnodes])


def parse(src, fmt, std):

    def _split(_src):
        _lines = []
        s = 0
        for e in range(len(_src)):
            if _src[e] == '\n':
                _lines.append(_src[s:e+1])
                s = e + 1
        return _lines

    ###############################
    ######### preprocess ##########
    ###############################

    lines = _split(src)

    # handle comments
    cmt_linemap, lines = handle_comments(lines, fmt, std)

    #...

    # update linemap to start from 1
    #linemap = dict((k+1, v+1) for k, v in linemap.items())

    ###############################
    #########    parse   ##########
    ###############################

    lexer = Cobol85Lexer(InputStream(''.join(lines)))
    stream = CommonTokenStream(lexer)
    parser = Cobol85Parser(stream)
    tree = parser.startRule()
    root = Node(attrs=OrderedDict(), shared_methods={'tocobol': tocobol_proxy})
    listner = Cobol85Listener(root, stream)
    walker = ParseTreeWalker()
    walker.walk(listner, tree)

    return root

def handle_comments(_lines, fmt, std):

    linemap = {}

    def _handle_cmtentry(_line):
        for pattern in cmtentry_patterns:
            match = pattern.match(_line)
            if match:
                cmtentry = match.group('cmtentry').strip()
                if cmtentry:
                    _line = _line.replace(cmtentry, '*>CE %s'%cmtentry)
                    break
        return _line

    lines = []
    for lineno, line in enumerate(_lines):
        ind = -1
        if fmt == FIXED_FORMAT:
            if len(line) >= 7:
                ind = 6
        elif fmt == FREE_FORMAT:
            if len(line) >= 1:
                ind = 0
        elif fmt == VARIABLE_FORMAT:
            raise NotImplemented('VARIABLE format is not supported yet.')

        if ind >= 0:
            if line[ind] == '*':
                if not line[ind:].startswith('*>'):
                    line = '*> '+line[ind+1:]
            elif line[ind] in ('$', 'D', 'd', '/'):
                line = '*> '+line[ind:]
            else:
                line = _handle_cmtentry(line[ind+1:])
            linemap[lineno] = line[:ind]
        else:
            linemap[lineno] = None

        lines.append(line)

    return linemap, lines

