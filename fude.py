#  fude.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2012 Jun Kikuchi. All rights reserved.
#
from xml.sax.saxutils import escape

def html(data):
    if isinstance(data, list):
        if data == []:
            return ''
        if isinstance(data[0], list):
            return ''.join([html(a) for a in data])

        xs_class = data.pop(0).split('.')
        xs_id = xs_class.pop(0).split('#')
        tag = xs_id.pop(0) or 'div'

        _attrs = {}
        if xs_id <> []:
            _attrs['id'] = xs_id.pop(0)
        if xs_class <> []:
            _attrs['class'] = ' '.join(xs_class)
        if data <> [] and isinstance(data[0], dict):
            _attrs.update(data.pop(0))

        attrs = ''
        if _attrs <> {}:
            attrs = ' ' + ' '.join([
                '%s="%s"' % (escape(k), escape(_attrs[k]))
                    for k in sorted(_attrs.keys())])

        if data <> []:
            container = [html(a) for a in data]
            return '<%s%s>%s</%s>' % (tag, attrs, ''.join(container), tag)
        else:
            return '<%s%s />' % (tag, attrs)
    else:
        return str(data)
