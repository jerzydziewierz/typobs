# setup.py as described in:
# https://stackoverflow.com/questions/27494758/how-do-i-make-a-python-script-executable
# to install on your system, run:
# > pip install -e .

from setuptools import setup, find_packages
setup(
    name='typobs',
    version='0.0.3',
    entry_points={
        'console_scripts': [
            'to_obsidian=to_obsidian:run',
            'to_typora=to_typora:run',
        ]
    },
    packages=find_packages(),
    # metadata to display on PyPI
    author="Jerzy Dziewierz",
    author_email="jurek_pypi@dziewierz.pl",
    description="Convert between Typora and Obsidian link styles",
    keywords="Typora Obsidian Markdown link converter",
    url="https://github.com/jerzydziewierz/typobs",   # project home page, if any
    project_urls={
        "Bug Tracker": "https://github.com/jerzydziewierz/typobs",
        "Documentation": "https://github.com/jerzydziewierz/typobs",
        "Source Code": "https://github.com/jerzydziewierz/typobs",
    },
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
        "Topic :: Office/Business",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing :: Markup",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
    ]
)