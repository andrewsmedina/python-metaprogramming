from lxml import html


def html_minify(html_code):
    dom = html.fromstring(html_code)
    return html.tostring(dom)



def test(code):
    return html_minify(code)


# @minify
# def test2(code):
#     return code


pure = "<html>    <body>  <body>   </html>"
minified = "<html><body>     </body></html>"

assert minified == test(pure)
# assert minified == test2(pure)
