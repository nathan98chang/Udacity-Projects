import os

import jinja2
import webapp2

#jinja loading syntax
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#notice the autoescape flag used to escape html inputs
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), 
    autoescape = True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        items = self.request.get_all("food")
        self.render('shoppinglist.html', items = items)



app = webapp2.WSGIApplication([('/', MainPage)], debug=True)