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
Abstract representation of Brainfuck source code.
"""

import re


class SourceCode:
    """
    Initially parsed and validated instructions.
    """

    @classmethod
    def from_file(cls, path):
        """Return instance of brainf.SourceCode."""
        with open(path) as file_object:
            return cls(file_object.read())

    def __init__(self, text):
        """Normalize and parse plain text."""
        self.instructions = normalize(text)
        self.jumps = parse(self.instructions)

    def __len__(self):
        """Return the total number of instructions."""
        return len(self.instructions)

    def __getitem__(self, index):
        """Return instruction at the given index."""
        return self.instructions[index]


def normalize(text):
    """Strip anything but valid instructions."""
    return re.sub(r'[^.,<>+\-\[\]]+', '', text)


def parse(instructions):
    """Return a dict with indices of matching brackets."""
    jumps = {}
    try:
        stack = []
        for i, instruction in enumerate(instructions):
            if instruction == '[':
                stack.append(i)
            elif instruction == ']':
                j = stack.pop()
                jumps[i], jumps[j] = j, i
    except IndexError:
        raise SyntaxError(f'unbalanced brackets at position {i}')
    else:
        return jumps
