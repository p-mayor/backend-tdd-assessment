#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "peter mayor"


import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser()
    # parser.add_argument('-h/--help', help="show this help message and exit")
    parser.add_argument('-u','--upper', metavar='', help="convert text to uppercase")
    parser.add_argument('-l','--lower', metavar='', help="convert text to lowercase")
    parser.add_argument('-t','--title', metavar='', help="convert text to titlecase")
    return parser.parse_args()



def main():
    """Implementation of echo"""
    args = create_parser()
    # print args
    


if __name__ == '__main__':
    main()
