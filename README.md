Bibtex Painkiller
=================

This is a script to make retrieving Bibtex entries less painful and to ensure that the entries look reasonably uniform. The motivation came from the shortcomings of bibliography managers that either lack matching functionality or they don’t bother ensuring uniform formatting. It is a painkiller rather than a complete solution. The script has two functionalities:

1. Retrieve Bibtex for an arXiv ID or a DOI. If the arXiv entry includes a DOI, it will retrieve a complete Bibtex including the DOI and arXiv information. All types of entries are postprocessed to give them a uniform look, primarily targetting Revtex 4.1.

2. Find the PDF on the filesystem given a Bibtex ID. The search starts from the current working directory. This helps adding a file field to the Bibtex entry.

There are two ways of invoking the script:

1. Passing the identifier as an argument:

    $ bibpain.py arXivID
    $ bibpain.py DOI

The arXiv ID should come without “arXiv:” and without version information. The DOI should be the actual DOI, and not the URL to the resolver.

2. Pasting from the clipboard:

    $ bibpain.py | xclip -selection clipboard

This is useful if you want to assign a keyboard shortcut to using it.
