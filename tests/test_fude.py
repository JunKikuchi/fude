import unittest
from fude import html

class HTMLTextCase(unittest.TestCase):
    def test_escape_attrs(self):
        data = ['tag#<>.<>']
        expt = '<tag class="&lt;&gt;" id="&lt;&gt;" />'
        self.assertEqual(html(data), expt)

    def test_tag(self):
        data = []
        expt = ''
        self.assertEqual(html(data), expt)

        data = ['tag']
        expt = '<tag />'
        self.assertEqual(html(data), expt)

        data = ['100']
        expt = '<100 />'
        self.assertEqual(html(data), expt)

        data = ['tag#id']
        expt = '<tag id="id" />'
        self.assertEqual(html(data), expt)

        data = ['tag.class']
        expt = '<tag class="class" />'
        self.assertEqual(html(data), expt)

        data = ['tag.class.a']
        expt = '<tag class="class a" />'
        self.assertEqual(html(data), expt)

        data = ['tag#id.class']
        expt = '<tag class="class" id="id" />'
        self.assertEqual(html(data), expt)

        data = ['tag#id.class.a']
        expt = '<tag class="class a" id="id" />'
        self.assertEqual(html(data), expt)

        data = ['tag', {'data': 'aaa'}]
        expt = '<tag data="aaa" />'
        self.assertEqual(html(data), expt)

        data = ['tag', {'data': 'aaa', 'id': 'id', 'class': 'class'}]
        expt = '<tag class="class" data="aaa" id="id" />'
        self.assertEqual(html(data), expt)

        data = ['tag#id.class', {'data': 'aaa'}]
        expt = '<tag class="class" data="aaa" id="id" />'
        self.assertEqual(html(data), expt)

        data = ['tag#id.class', {'data': 'aaa', 'id': 'ID', 'class': 'CLASS'}]
        expt = '<tag class="CLASS" data="aaa" id="ID" />'
        self.assertEqual(html(data), expt)

    def test_abbr_tag(self):
        data = ['#id']
        expt = '<div id="id" />'
        self.assertEqual(html(data), expt)

        data = ['.class']
        expt = '<div class="class" />'
        self.assertEqual(html(data), expt)

        data = ['.class.a']
        expt = '<div class="class a" />'
        self.assertEqual(html(data), expt)

        data = ['#id.class']
        expt = '<div class="class" id="id" />'
        self.assertEqual(html(data), expt)

        data = ['#id.class.a']
        expt = '<div class="class a" id="id" />'
        self.assertEqual(html(data), expt)

        data = ['', {'data': 'aaa'}]
        expt = '<div data="aaa" />'
        self.assertEqual(html(data), expt)

        data = ['', {'data': 'aaa', 'id': 'id', 'class': 'class'}]
        expt = '<div class="class" data="aaa" id="id" />'
        self.assertEqual(html(data), expt)

        data = ['#id.class', {'data': 'aaa'}]
        expt = '<div class="class" data="aaa" id="id" />'
        self.assertEqual(html(data), expt)

        data = ['#id.class', {'data': 'aaa', 'id': 'ID', 'class': 'CLASS'}]
        expt = '<div class="CLASS" data="aaa" id="ID" />'
        self.assertEqual(html(data), expt)

    def test_complex_tags(self):
        data = [['a'], ['b'], [''], []]
        expt = '<a /><b /><div />'
        self.assertEqual(html(data), expt)

        data = [['a', '100'], ['b', 200], [''], []]
        expt = '<a>100</a><b>200</b><div />'
        self.assertEqual(html(data), expt)

        data = ['html', []]
        expt = '<html></html>'
        self.assertEqual(html(data), expt)

        data = ['html', ['head'], ['body', ['p', 'hello world']]]
        expt = '<html><head /><body><p>hello world</p></body></html>'
        self.assertEqual(html(data), expt)

        data = ['html', ['head'], ['body', {'data': 'foobar'}, ['p#contents', 'hello world'], ['br.line'], 'foo', []]]
        expt = '<html><head /><body data="foobar"><p id="contents">hello world</p><br class="line" />foo</body></html>'
        self.assertEqual(html(data), expt)

if __name__ == "__main__":
    unittest.main()
