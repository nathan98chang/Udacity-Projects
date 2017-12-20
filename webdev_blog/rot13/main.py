# this is my version of the ROT13 homework on the Udacity 
# web dev tutorial
# copyright Nathan Chang
# changnat@usc.edu
import webapp2
import string
import cgi

form = """
<form method = "post">
    <p><b> Enter some text to ROT13: </b></p>
    <textarea name = "text">%(words)s</textarea>
    <br>
    <input type = "submit">
</form>
"""

# applies basic rot13 cryptography to letters in s using char arithmetic
# while also properly html escaping
def rot13hash(s):
    rot13_s = ""
    for letter in s:
        if letter in string.ascii_lowercase:
            if (ord(letter) + 13) > 122:
                rot13_s += chr(96 + ((ord(letter)+13)-122))
            else:
                rot13_s += chr(ord(letter) + 13)
        elif letter in string.ascii_uppercase:
            if (ord(letter) + 13) > 90:
                rot13_s += chr(64 + ((ord(letter)+13)-90))
            else:
                rot13_s += chr(ord(letter) + 13)
        else:
            rot13_s += letter
    return (cgi.escape(rot13_s, quote = True))

class MainPage(webapp2.RequestHandler):
    def write_form(self, text_ = ""):
        self.response.out.write(form % {"words" : text_})

    def get(self):
        self.write_form()

    def post(self):
        user_text = self.request.get("text")
        rot13_text = rot13hash(user_text)

        self.write_form(rot13_text)

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
