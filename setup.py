try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='bibpain',
    version='0.1',
    author='Peter Wittek',
    author_email='peterwittek@users.noreply.github.com',
    scripts=['scripts/bibpain.py'],
    url='https://github.com/peterwittek/bibpain/',
    keywords='bibtex doi arxiv',
    license='LICENSE',
    description=
    'Paste an arXiv ID or a DOI from the clipboard and receive the corresponding bibtex entry',
    long_description=open('README.md').read(),
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Development Status :: 4 - Beta', 'Programming Language :: Python'
    ],
    install_requires=["utf8tobibtex", "arxiv2bib", "pyperclip"])
