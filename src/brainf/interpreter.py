# The MIT License (MIT)
#
# Copyright (c) 2018 Bartosz Zaczynski
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
Brainfuck interpreter.
"""

import os
import sys

from brainf import SourceCode, Memory


def run(path):
    """Run interpreter against the given file using default memory."""
    interpret(SourceCode.from_file(path), Memory())


def interpret(code, memory):
    """Step through the code utilizing provided memory."""

    i = 0
    while i < len(code):

        instruction = code[i]

        if instruction == '+':
            memory.incr()
        elif instruction == '-':
            memory.decr()
        elif instruction == '>':
            memory.movf()
        elif instruction == '<':
            memory.movb()
        elif instruction == '.':
            put_char(memory)
        elif instruction == ',':
            get_char(memory)
        elif instruction == '[':
            if memory.cell == 0:
                i = code.jumps[i]
        elif instruction == ']':
            i = code.jumps[i]
            continue

        i += 1


def put_char(memory):
    """Print current cell's ASCII character on stdout."""
    if memory.cell == ord('\n'):
        print()  # produce platform specific newline
    else:
        print(chr(memory.cell), end='')


def get_char(memory):
    """Read next character from stdin and store it in memory.

    Return immediately when EOF.
    Skip extra newline characters, e.g. carriage return.
    Convert OS-specific newline to line feed.
    """

    char = sys.stdin.buffer.read(1)

    if len(char) > 0:
        if char in ('\r', '\n'):
            for _ in range(len(os.linesep) - 1):
                sys.stdin.buffer.read(1)
            char = '\n'
        memory.cell = ord(char)
