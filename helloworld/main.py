#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""main.py: console app which prints hello"""
import sys

def main(argv=None):
    """says Hello, world
       Returns: None
    """

    if argv is None:
        argv = sys.argv

    print("Hello, world")

    return None

if __name__ == '__main__':
    main()#testing
