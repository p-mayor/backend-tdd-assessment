#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "peter mayor with help from tyler"

import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument("-u", "--upper", help="convert text to uppercase",
                        action="store_true")
    parser.add_argument("-l", "--lower", help="convert text to lowercase",
                        action="store_true")
    parser.add_argument("-t", "--title", help="convert text to titlecase",
                        action="store_true")
    parser.add_argument("text", help="text to be manipulated")
    return parser


def to_upper(text):
    return text.upper()


def to_lower(text):
    return text.lower()


def to_title(text):
    return text.title()


def main():
    """Implementation of echo"""
    # namespace = create_parser()
    parser = create_parser()
    args = parser.parse_args()

    if args.upper:
        output = to_upper(args.text)
    if args.lower:
        output = to_lower(args.text)
    if args.title:
        output = to_title(args.text)
    if not args.upper and not args.lower and not args.title:
        output = args.text

    print output


if __name__ == '__main__':
    main()
