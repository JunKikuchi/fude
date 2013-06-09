#  fude.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2012-2013 Jun Kikuchi. All rights reserved.
#
from xml.sax.saxutils import escape
import types

def html(data):
    if isinstance(data, list):
        data = list(data)
        if data == []:
            return ''
        if isinstance(data[0], list):
            return ''.join([html(a) for a in data])

        xs_class = data.pop(0).split('.')
        xs_id = xs_class.pop(0).split('#')
        tag = xs_id.pop(0) or 'div'

        _attrs = {}
        if xs_id != []:
            _attrs['id'] = xs_id.pop(0)
        if xs_class != []:
            _attrs['class'] = ' '.join(xs_class)
        if data != [] and isinstance(data[0], dict):
            if 'id' in data[0]:
                _attrs['id'] = data[0].pop('id')
            if ('class' in data[0]) and ('class' in _attrs):
                _attrs['class'] += ' ' + data[0].pop('class')
            _attrs.update(data.pop(0))

        attrs = ''
        if _attrs != {}:
            attrs = ' ' + ' '.join([
                '%s="%s"' % (escape(k), escape(_attrs[k])) if _attrs[k] else escape(k)
                    for k in sorted(_attrs.keys())])

        if data != []:
            container = [html(a) for a in data]
            return '<%s%s>%s</%s>' % (tag, attrs, ''.join(container), tag)
        else:
            return '<%s%s />' % (tag, attrs)
    if isinstance(data, types.FunctionType):
        return data()
    else:
        return escape(data)
