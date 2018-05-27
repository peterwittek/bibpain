try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='gen_bibtex',
    version='0.1',
    author='Peter Wittek',
    author_email='peterwittek@users.noreply.github.com',
    scripts=['scripts/gen_bibtex'],
    url='https://github.com/peterwittek/gen_bibtex/',
    keywords='bibtex doi arxiv',
    license='LICENSE',
    description='Paste an arXiv ID or a DOI from the clipboard and receive the corresponding bibtex entry',
    long_description=open('README.md').read(),
    classifiers=[
         'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
         'Operating System :: OS Independent',
         'Intended Audience :: End Users/Desktop',
         'Development Status :: 4 - Beta',
         'Programming Language :: Python'
    ],
    install_requires=[
        "utf8tobibtex",
        "arxiv2bib",
        "pyperclip"
    ]
)
