import io
import os.path
from setuptools import setup

VERSION_PATH = os.path.join(
    os.path.dirname(__file__), 'helloworld/VERSION.txt')
with io.open(VERSION_PATH, 'r', encoding='utf-8') as f:
  version = f.read().strip()

setup(
    name = "helloworld",        # what you want to call the archive/egg
    version = version,
    packages=["helloworld"],    # top-level python modules you can import like
                                #   'import foo'
    dependency_links = [],      # custom links to a specific project
    install_requires=[],
    extras_require={},      # optional features that other packages can require
                            #   like 'helloworld[foo]'
    package_data = {"helloworld": ["VERSION.txt"]},
    author="David Barnett",
    author_email = "davidbarnett2@gmail.com",
    description = "The familiar example program in Python",
    license = "Apache 2.0",
    keywords= "example documentation tutorial",
    url = "http://github.com/dbarnett/python-helloworld",
    entry_points = {
        "console_scripts": [        # command-line executables to expose
            "helloworld_in_python = helloworld.main:main",
        ],
        "gui_scripts": []       # GUI executables (creates pyw on Windows)
    }
)
