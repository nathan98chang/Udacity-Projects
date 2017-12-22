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

#HTML code for the form
form = """
<form method = "post">
    <h2><b>Signup</b></h2>
    <table>
      <tbody>
        <tr>
        <td><label>Username</label></td>
        <td><input type = "text" name = "username">%(username)s</td>
        <td>%(usererror)s</td>
        </tr>
        
        <tr>
        <td><label>Password</label></td>
        <td><input type = "password" name = "password">%(password)s</td>
        <td>%(passerror)s</td>
        </tr>
        
        <tr>
        <td><label>Verify Password</label></td>
        <td><input type = "password" name = "verify">%(verify)s</td>
        <td>%(verifyerror)s</td>
        </tr>
        
        <tr>
        <td><label>Email (optional)</label></td>
        <td><input type = "text" name = "email">%(email)s</td>
        <td>%(emailerror)s</td>
        </tr>
      </tbody>
    </table>
    
    <input type = "submit">
</form>
"""

#HTML code for success page
success = """
<h1><b>Welcome %(username)s!</b></h1>
"""

class MainPage(webapp2.RequestHandler):
    def write_form(self, user = "", pw = "", ver = "", eml = "",
        usererr = "", pwerr = "", verifyerr = "", emailerr = ""):
        self.response.out.write(form % {"username": user,
                                        "password": pw,
                                        "verify": ver,
                                        "email": eml,
                                        "usererror": usererr,
                                        "passerror": pwerr,
                                        "verifyerror": verifyerr,
                                        "emailerror": emailerr})

    def get(self):
        self.write_form()

    def post(self):
        user_name = self.request.get("username")
        user_pass = self.request.get("password")
        user_verify = self.request.get("verify")
        user_email = self.request.get("email")

        if valid_username(user_name) and valid_password(user_pass) and valid_email(user_email) and user_pass == user_verify:
            # redirect to success page
            self.redirect("/success")
        else:
            if not valid_username(user_name):
                pass
            if not valid_password(user_pass):
                pass
            if not (user_pass == user_verify):
                pass
            if not valid_email(user_email):
                pass


class SuccessHandler(webapp2.RequestHandler):
    def get(self, user = ""):
        self.response.out.write(success % {"username": user})


app = webapp2.WSGIApplication([('/', MainPage), ('/success', SuccessHandler)], debug=True)
