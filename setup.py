import io
import os.path
from setuptools import setup

VERSION_PATH = os.path.join(
    os.path.dirname(__file__), 'helloworld/VERSION.txt')
with io.open(VERSION_PATH, 'r', encoding='utf-8') as f:
  version = f.read().strip()

setup(
    version = version,
)
