# -*- coding: utf-8 -*-
from distutils.core import setup
setup(
    name = "fude",
    py_modules = ["fude"],
    version = "1.0.1",
    description = "Library for rendering HTML in Python",
    author = "Jun Kikuchi",
    author_email = "kikuchi@bonnou.com",
    url = "https://github.com/JunKikuchi/fude",
    download_url = "http://pypi.python.org/packages/source/f/fude/fude-1.0.1.tar.gz",
    keywords = ["html"],
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
        ],
    long_description = """\
Fude (筆)
=========

Fude (筆) is a library for representing HTML in Python. It uses Lists to
represent elements, and Dicts to represent an element’s attributes.

Fude is inspired by Hiccup https://github.com/weavejester/hiccup

Syntax
------

Here is a basic example of Fude syntax:

::

    >>> fude.html('text')
    'text'

    >>> fude.html(['tag'])
    '<tag />'

    >>> fude.html(['div', 'bar'])
    '<div>bar</div>'

    >>> fude.html(['span', {'class': 'foo'}, 'bar'])
    '<span class="foo">bar</span>'

    >>> fude.html(['div', 'bar', ['span', 'baz'], ['span', 'bang']])
    '<div>bar<span>baz</span><span>bang</span></div>'

    >>> fude.html(['div', 'bar', [['span', 'baz'], ['span', 'bang']]])
    '<div>bar<span>baz</span><span>bang</span></div>'

The first element of the List is used as the element name. The second
attribute can optionally be a Dict, in which case it is used to supply
the element’s attributes. Every other element is considered part of the
tag’s body.

And provides a CSS-like shortcut for denoting ``id`` and ``class``
attributes:

::

    >>> fude.html(['div#foo.bar.baz', 'bang'])
    '<div class="bar baz" id="foo">bang</div>'

    >>> fude.html(['#foo.bar.baz', 'bang'])
    '<div class="bar baz" id="foo">bang</div>'

If the body of the element is a List, its contents will be expanded out
into the element body. This makes working with functions like ``map``
and ``List comprehensions``:

::

    >>> fude.html(['ul', [['li', x] for x in range(1, 4)]])
    '<ul><li>1</li><li>2</li><li>3</li></ul>'
"""
)
