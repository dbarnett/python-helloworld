import argparse
import sys

import helloworld
import parser


def hello_world():
    print("Hello, world")


def main(argv=None):
    if argv is None:
        argv = sys.argv

    # The helloworld program doesn't expect any arguments.
    # This just checks for the special --version and --help arguments and
    # ensures the user hasn't passed any other unrecognized arguments.
    parser.parse_args(argv[1:])

    hello_world()

    return 0
