#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess

to_upper = echo.to_upper
to_lower = echo.to_lower
to_title = echo.to_title
create_parser = echo.create_parser


class TestEcho(unittest.TestCase):
    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper(self):
        """ Check that upper works """
        self.assertEqual(to_upper('hello'), 'HELLO')

    def test_lower(self):
        """ Check that lower works """
        self.assertEqual(to_lower('HELLO'), 'hello')

    def test_title(self):
        """ Check that title works """
        self.assertEqual(to_title('hello'), 'Hello')

    def test_empty(self):
        """ Check empty args"""
        process = subprocess.Popen(
            ["python", "./echo.py", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        self.assertEquals(stdout, "hello")

    def test_parser(self):
        parser = create_parser()
        args_list = ['-ult', 'hello']

        name_space = parser.parse_args(args_list)

        self.assertTrue(name_space.upper)
        self.assertTrue(name_space.lower)
        self.assertTrue(name_space.title)


if __name__ == '__main__':
    unittest.main()
