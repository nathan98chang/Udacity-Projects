# this is my version of the user signup homework on the Udacity 
# web dev tutorial
# copyright Nathan Chang
# changnat@usc.edu
import webapp2


class MainPage(webapp2.RequestHandler):
    




app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
