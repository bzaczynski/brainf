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

import unittest

import brainf.memory


class TestMemory(unittest.TestCase):

    def setUp(self):
        self.memory = brainf.memory.Memory()

    def test_should_allocate_default_size(self):
        self.assertEqual(65536, len(self.memory.cells))

    def test_should_allocate_custom_size(self):
        memory = brainf.memory.Memory(16)
        self.assertEqual(16, len(memory.cells))

    def test_should_init_pointer_at_zero(self):
        self.assertEqual(0, self.memory.pointer)

    def test_should_get_current_cell_value(self):

        # given
        self.memory.pointer = 42
        self.memory.cells[42] = 127

        # then
        self.assertEqual(127, self.memory.cell)

    def test_should_set_current_cell_value(self):

        # given
        self.memory.pointer = 42

        # when
        self.memory.cell = 127

        # then
        self.assertEqual(127, self.memory.cells[42])

    def test_should_increment_value_at_current_cell(self):

        # given
        self.memory.pointer = 42
        self.memory.cell = 127

        # when
        self.memory.incr()

        # then
        self.assertEqual(128, self.memory.cell)

    def test_should_decrement_value_at_current_cell(self):

        # given
        self.memory.pointer = 42
        self.memory.cell = 127

        # when
        self.memory.decr()

        # then
        self.assertEqual(126, self.memory.cell)

    def test_should_move_pointer_forward(self):

        # given
        self.memory.pointer = 42

        # when
        self.memory.movf()

        # then
        self.assertEqual(43, self.memory.pointer)

    def test_should_move_pointer_backwards(self):

        # given
        self.memory.pointer = 42

        # when
        self.memory.movb()

        # then
        self.assertEqual(41, self.memory.pointer)

    def test_should_overflow(self):

        # given
        self.memory.pointer = len(self.memory.cells) - 1

        # then
        with self.assertRaises(MemoryError):
            # when
            self.memory.movf()

    def test_should_underflow(self):

        # given
        self.memory.pointer = 0

        # then
        with self.assertRaises(MemoryError):
            # when
            self.memory.movb()


if __name__ == '__main__':
    unittest.main()
