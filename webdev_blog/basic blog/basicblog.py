import os
import webapp2
import jinja2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
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

#the database
class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

#this class handles permalink redirection ie. having links to a single post
class PermalinkHandler(Handler):
    def get(self, the_id):
        entry = Post.get_by_id(long(the_id))
        if entry:
            self.render("singlepost.html", entry = entry)

#class to handle adding new entries to the blog
class NewEntry(Handler):
    def get(self, subject="", content="", error=""):
        self.render("submission.html", subject=subject, content=content, error=error)

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")

        if subject and content:
            #create an entity
            entry = Post(subject = subject, content = content)
            #store it in the database
            entry.put()
            #and redirect to the permalink containing the post
            the_id = str(entry.key().id())
            self.redirect('/blog/%s' % the_id)
        else:
            error = "subject AND content, por favor"
            self.get(subject=subject, content=content, error=error)


class MainPage(Handler):
    #renders front page of blog, showing any entries in the database
    def render_front(self):
        entries = db.GqlQuery("SELECT * from Post "
                           "ORDER BY created DESC ")

        self.render("frontpage.html", entries = entries)

    def get(self):
        self.render_front()


app = webapp2.WSGIApplication([('/blog', MainPage), ('/blog/newpost', NewEntry), ('/blog/([0-9]+)', PermalinkHandler)], debug=True)


