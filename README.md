# Fude (筆)

Fude (筆) is a library for representing HTML in Python. It uses Lists
to represent elements, and Dicts to represent an element's attributes.

Fude is inspired by Hiccup <https://github.com/weavejester/hiccup>

## Syntax

Here is a basic example of Fude syntax:

```python
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
```

The first element of the List is used as the element name. The second
attribute can optionally be a Dict, in which case it is used to supply
the element's attributes. Every other element is considered part of the
tag's body.

And provides a CSS-like shortcut for denoting `id` and `class`
attributes:

```python
>>> fude.html(['div#foo.bar.baz', 'bang'])
'<div class="bar baz" id="foo">bang</div>'

>>> fude.html(['#foo.bar.baz', 'bang'])
'<div class="bar baz" id="foo">bang</div>'
```

If the body of the element is a List, its contents will be expanded out
into the element body. This makes working with functions like `map` and
`List comprehensions`:

```python
>>> fude.html(['ul', [['li', x] for x in range(1, 4)]])
'<ul><li>1</li><li>2</li><li>3</li></ul>'
```

## Authors

Jun Kikuchi

## Copyright

Copyright (c) 2012 Jun Kikuchi. See LICENSE for details.
