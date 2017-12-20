# this is my version of the user signup homework on the Udacity 
# web dev tutorial
# copyright Nathan Chang
# changnat@usc.edu
import webapp2
import re


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



class MainPage(webapp2.RequestHandler):





app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
