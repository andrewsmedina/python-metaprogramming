minify
======

minify html response for django views.

eg:

    def index(response):
        response = render_to_response("index.html")
        return minify(response)

    def contact(response):
        html = "<html>  <body>"
        html += "<h1>contact  </h1>"
        html += "</body>   </html>"
        response = HttpResponse(html)
        return minify(HttpResponse)

solution
========

use decorators:

    @minify
    def index(response):
        return render_to_response("index.html")

    @minify
    def contact(response):
        html = "<html>  <body>"
        html += "<h1>contact  </h1>"
        html += "</body>   </html>"
        return HttpResponse(html)
