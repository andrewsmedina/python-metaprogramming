from lxml import html

from functools import wraps


def html_minify(html_code):
    dom = html.fromstring(html_code)
    return html.tostring(dom)


def minify(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        html_code = func(*args, **kwargs)
        return html_minify(html_code)
    return wrapper


def test(code):
    return html_minify(code)


@minify
def test2(code):
    return code


pure = "<html>    <body>  <body>   </html>"
minified = "<html><body>     </body></html>"

assert minified == test(pure)
assert minified == test2(pure)
