import os
import webapp2
import jinja2
import hmac
import re

#used for HMAC "salting"
SECRET = 'imsosecret'

# input verification functions based on given parameters from write-up
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def valid_username(username):
    return USER_RE.match(username)
def valid_password(password):
    return PASS_RE.match(password)
def valid_email(email):
    return EMAIL_RE.match(email)

#gae database jargon
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), 
    autoescape = True)

#hash verification functions
import hashlib

def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()

def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
    ###Your code here
    original = h.split('|')[0]
    if make_secure_val(original) == h:
        return original

#class for the database


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self, username="", password="", verify="", email="", usererror="", 
        passerror="", verifyerror="", emailerror=""):

        self.render("signup.html", username=username, password="",
            verify="", email=email, usererror=usererror, passerror=passerror,
            verifyerror=verifyerror, emailerror=emailerror)

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        if valid_username(username) and valid_password(password) and password == verify and valid_email(email):
            self.render("welcome.html", username=username)
        else:
            error1 = ""
            error2 = ""
            error3 = ""
            error4 = ""

            if not valid_username(username):
                error1 = "That's not a valid username."
            if not valid_password(password):
                error2 = "That wasn't a valid password."
            if not (password == verify):
                error3 = "Your passwords didn't match."
            if not valid_email(email):
                error4 = "That's not a valid email."

            self.render("signup.html", username=username, password="",
                verify="", email=email, usererror=error1, passerror=error2,
                verifyerror=error3, emailerror=error4)


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)




