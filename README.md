mess
====

mess is a console file-sharing tool, which allows you to easily send links to a couple of files to somebody.

It requires ssh connection to a publicly visible web server.

Here is an example. I want to show a picture to a friend, let's say `me-in-pijamas.jpg`. I run:

    $ mess me-in-pijamas.jpg
    Shared files:
    http://nikolay.bg/mess/me-in-pijamas.jpg (copied in clipboard)

I have configured mess to copy the files to the mess directory to my hosting,
so that the file is publicy visible.

In Mac OS X, it also copies the first URL to the clipboard, so that sharing is only a paste away.

Installation
============

After you have checked out the repository, run:

    $ python setup.py install

or if you want it install in a different prefix:

    $ python setup.py install --prefix=$HOME


Configuration
=============

The default configuration file is in `$HOME/.mess`. There you can specify the connection details and the URL for you files.