# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

"""Main module."""

import re
from collections import OrderedDict, MutableMapping
from io import StringIO

from antlr4 import (InputStream, CommonTokenStream, ParseTreeWalker,
    BufferedTokenStream, ParserRuleContext, TerminalNode, Token)
from .parser.Cobol85Lexer import Cobol85Lexer
from .parser.Cobol85Listener import Cobol85Listener
from .parser.Cobol85Parser import Cobol85Parser

from stemtree import Node, SourceLines

EOF = Token.EOF
EPSILON = Token.EPSILON

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

#def packline(obj, text):
#
#    main_text = obj.seq_area + obj.ind_area + text
#    # TODO: conform
#    lines = _conform_format(main_text, obj.sourceformat)
#    if obj.ext_area:
#        lines[-1] += ' '*(72-len(lines[-1])) + obj.ext_area
#    return '\n'.join(lines)

def tocobol(obj, revise=None):

    if hasattr(obj, 'text'):
        if obj.text in ('\n',):
            lnode = obj.get_leftnode()
            if isinstance(lnode, obj.__class__) and hasattr(lnode, 'text') and \
                lnode.text.startswith('*> __stemcobol__'):
                return ''
            else:
                return obj.text
        elif obj.text.startswith('*> __stemcobol__'):
            direct, text = obj.text[16:].split(':', 1)
            if direct in ('seq', 'ext'):
                return text
            elif direct.startswith('ind'):
                return  direct[3]+text
            else:
                import pdb; pdb.set_trace()
        elif revise:
            #return obj.packline(revise(obj))
            return revise(obj)
        else:
            #return obj.packline(obj.text)
            return obj.text

    return ''.join([c.tocobol(revise=revise) for c in obj.subnodes])

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
    lines = preprocess(lines, fmt, std)

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
    shared_methods = {'tocobol': tocobol, 'packline': packline}
    root = Node(attrs=OrderedDict(), shared_methods=shared_methods)
    listner = Cobol85Listener(root, stream)
    walker = ParseTreeWalker()
    walker.walk(listner, tree)

    return root

def preprocess(_lines, fmt, std):

    def _handle_cmtentry(_line):
        for pattern in cmtentry_patterns:
            match = pattern.match(_line)
            if match:
                cmtentry = match.group('cmtentry').strip()
                if cmtentry:
                    _line = _line.replace(cmtentry, '*>CE __stemcobol__:'+cmtentry)
                    break
        return _line

    seq = None
    ind = None
    ext = None

    if fmt == FIXED_FORMAT:
        seq = (0, 6)
        ind = (6, 7)
        ext = (72, None)
    elif fmt == FREE_FORMAT:
        ind = (0, 1)
    elif fmt == VARIABLE_FORMAT:
        raise NotImplemented('VARIABLE format is not supported yet.')

    lines = []
    for lineno, line in enumerate(_lines):

        L = len(line)

        if seq:
            lines.append('*> __stemcobol__seq:%s\n'%line[seq[0]:seq[1]])

        if ind and ind[0] < L:
            if line[ind[0]] == '-':
                import pdb; pdb.set_trace()
            elif line[ind[0]] == '*':
                if not line[ind[0]:].startswith('*>'):
                    line = '*> __stemcobol__ind*:%s\n'%line[ind[1]:]
            elif line[ind[0]] in ('$', 'D', 'd', '/'):
                line = '*> __stemcobol__ind%s:%s\b'%(line[ind[0]], line[ind[1]:])
            else:
                line = _handle_cmtentry(line[ind[0]:])

        if ext and ext[0] < L:
            lines.append('*> __stemcobol__ext:%s\n'%line[ext[0]:ext[1]])
        lines.append(line)

    return lines
