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
from unittest.mock import patch, mock_open, PropertyMock

import io

import brainf
import brainf.interpreter


@patch('builtins.open', mock_open())
class TestRun(unittest.TestCase):

    @patch('brainf.interpreter.interpret')
    def test_should_create_default_memory(self, mock_interpret):

        # when
        brainf.interpreter.run('/fake/path/to/file.b')

        # then
        (code, memory), kwargs = mock_interpret.call_args
        self.assertEqual(65536, len(memory.cells))

    @patch('brainf.SourceCode.from_file')
    def test_should_load_source_code_from_file(self, mock_from_file):

        # when
        brainf.interpreter.run('/fake/path/to/file.b')

        # then
        mock_from_file.assert_called_once_with('/fake/path/to/file.b')

    @patch('brainf.interpreter.interpret')
    def test_should_run_interpreter(self, mock_interpret):

        # when
        brainf.interpreter.run('/fake/path/to/file.b')

        # then
        mock_interpret.assert_called_once()


class TestInterpret(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_should_interpret_code(self, mock_stdout):

        # given
        code = brainf.SourceCode('++++++++++[>++++++<-]>+++++.')
        memory = brainf.Memory()

        # when
        brainf.interpret(code, memory)

        # then
        self.assertEqual('A', mock_stdout.getvalue())
        self.assertEqual(1, memory.pointer)
        self.assertEqual(65, memory.cells[1])


@patch('sys.stdout', new_callable=io.StringIO)
class TestPutChar(unittest.TestCase):

    def test_should_print_regular_character(self, mock_stdout):

        # given
        memory = brainf.Memory()
        memory.cell = 65

        # when
        brainf.interpreter.put_char(memory)

        # then
        self.assertEqual('A', mock_stdout.getvalue())

    def test_should_print_newline(self, mock_stdout):

        # given
        memory = brainf.Memory()
        memory.cell = 10

        # when
        brainf.interpreter.put_char(memory)

        # then
        self.assertEqual('\n', mock_stdout.getvalue())


class TestGetChar(unittest.TestCase):

    def setUp(self):
        self.memory = brainf.Memory()

    @patch('sys.stdin.buffer.read', return_value='')
    def test_should_do_nothing_on_end_of_file(self, _):

        # given
        self.memory.cell = 127

        # when
        brainf.interpreter.get_char(self.memory)

        # then
        self.assertEqual(127, self.memory.cell)

    @patch('sys.stdin.buffer.read', side_effect=['\r', '\n'])
    @patch('os.linesep', '\r\n')
    def test_should_handle_newline_on_windows(self, _):

        # when
        brainf.interpreter.get_char(self.memory)

        # then
        self.assertEqual(10, self.memory.cell)

    @patch('sys.stdin.buffer.read', side_effect=['\r'])
    @patch('os.linesep', '\r')
    def test_should_handle_newline_on_mac(self, _):

        # when
        brainf.interpreter.get_char(self.memory)

        # then
        self.assertEqual(10, self.memory.cell)

    @patch('sys.stdin.buffer.read', side_effect=['\n'])
    @patch('os.linesep', '\n')
    def test_should_handle_newline_on_linux(self, _):

        # when
        brainf.interpreter.get_char(self.memory)

        # then
        self.assertEqual(10, self.memory.cell)

    @patch('sys.stdin.buffer.read', return_value='A')
    def test_should_handle_regular_character(self, _):

        # when
        brainf.interpreter.get_char(self.memory)

        # then
        self.assertEqual(65, self.memory.cell)


if __name__ == '__main__':
    unittest.main()
