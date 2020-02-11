# -*- coding: UTF-8 -*-
"""main.py: A console app, it prints hello world"""
import sys

def main(argv=None) -> None:
    """prints Hello, world
       Returns: None
    """

    if argv is None:
        argv = sys.argv
        
    print("Hello, world")

    return 0
