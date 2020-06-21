# setup.py as described in:
# https://stackoverflow.com/questions/27494758/how-do-i-make-a-python-script-executable
# to install on your system, run:
# > pip install -e ./
from setuptools import setup
setup(
    name='typobs',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'to_obsidian=to_obsidian:run',
            'to_typora=to_typora:run',
        ]
    }
)