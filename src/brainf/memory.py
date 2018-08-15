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
Memory used for the execution of Brainfuck programs.
"""


class Memory:
    """Fixed size virtual memory comprised of cells."""

    def __init__(self, num_bytes=2**16):
        """Initialize memory with zeros."""
        self.cells = [0] * num_bytes
        self.pointer = 0

    @property
    def cell(self):
        """Return value from the current cell."""
        return self.cells[self.pointer]

    @cell.setter
    def cell(self, value):
        """Assign value to the current cell."""
        self.cells[self.pointer] = value

    def incr(self):
        """Increment value at the current cell."""
        self.cell = self.cell + 1

    def decr(self):
        """Decrement value at the current cell."""
        self.cell = self.cell - 1

    def movf(self):
        """Move pointer forward or raise MemoryError."""
        self.pointer = self.pointer + 1
        if self.pointer >= len(self.cells):
            raise MemoryError('not enough memory')

    def movb(self):
        """Move pointer backwards or raise MemoryError."""
        self.pointer = self.pointer - 1
        if self.pointer < 0:
            raise MemoryError('negative memory address')
