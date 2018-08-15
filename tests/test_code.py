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
from unittest.mock import patch, mock_open

import brainf.code


class TestNormalize(unittest.TestCase):

    def test_should_retain_only_valid_instructions(self):
        plain_text = ' \t a1]Ab2 .Bc3 Cd4<D\n[e5-Ef6\nFg,\n>7Gh8H + '
        self.assertEqual('].<[-,>+', brainf.code.normalize(plain_text))


class TestParse(unittest.TestCase):

    def test_should_return_bidirectional_map_of_loop_jumps(self):

        # given
        instructions = '+++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.'

        # when
        jumps = brainf.code.parse(instructions)

        # then
        self.assertDictEqual(jumps, {

            3: 43,
            43: 3,

            9: 28,
            28: 9,

            38: 40,
            40: 38
        })

    def test_should_raise_syntax_error_on_unbalanced_brackets(self):
        with self.assertRaises(SyntaxError):
            brainf.code.parse('][')

    def test_should_raise_syntax_error_on_missing_opening_bracket(self):
        with self.assertRaises(SyntaxError):
            brainf.code.parse(']')

    @unittest.skip("Not yet implemented")  # TODO
    def test_should_raise_syntax_error_on_missing_closing_bracket(self):
        with self.assertRaises(SyntaxError):
            brainf.code.parse('[')

    @unittest.skip("Not yet implemented")  # TODO
    def test_should_raise_syntax_error_on_incorrectly_nested_brackets(self):
        with self.assertRaises(SyntaxError):
            brainf.code.parse('[[[]')


class TestSourceCode(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.plain_text = 'foo: ++++[>+++<-]>++.'

    @patch('brainf.code.normalize')
    def test_should_normalize_code(self, mock_normalize):

        # when
        brainf.code.SourceCode(self.plain_text)

        # then
        mock_normalize.assert_called_once_with(self.plain_text)

    @patch('brainf.code.parse', return_value={4: 11, 11: 4})
    def test_should_parse_code(self, mock_parse):

        # when
        source_code = brainf.code.SourceCode(self.plain_text)

        # then
        mock_parse.assert_called_once_with('++++[>+++<-]>++.')
        self.assertDictEqual(source_code.jumps, {4: 11, 11: 4})

    def test_should_return_number_of_instructions(self):
        source_code = brainf.code.SourceCode(self.plain_text)
        self.assertEqual(16, len(source_code))

    def test_should_get_instruction_at_index(self):
        source_code = brainf.code.SourceCode(self.plain_text)
        self.assertEqual('-', source_code[10])

    def test_should_load_from_file(self):

        # given
        with patch('builtins.open', mock_open(read_data=self.plain_text)) as mock_file:

            # when
            source_code = brainf.code.SourceCode.from_file('/fake/path/to/file.b')

            # then
            mock_file.assert_called_with('/fake/path/to/file.b')
            self.assertEqual('++++[>+++<-]>++.', source_code.instructions)
            self.assertDictEqual(source_code.jumps, {4: 11, 11: 4})


if __name__ == '__main__':
    unittest.main()
