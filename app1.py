from flask import Flask, redirect, url_for

app = Flask(__name__)

# this defines how flask will be told to access this func called home 
# in order to display the string in double quotes
# in flask this is called a route and it is created in python with a special 
# func called a decorator
# the text in quotes is what will be given to flask from the web browser or an API
# flask gets the text and compare it to its list of routes
# once flask gets a match, it runs the func that is associated with the matched text
# in this case, flask will received a "/", it checks the routes and runs the func 
# that matches "/"
# that func is supposed to return the attribute to the return command
# flask will then put the text in a format that the web browser or API can understand
@app.route("/")

# once this func is ran it will return page with the string written 
# inline html can be passed  in the return
def home():
    return "welcome to app1 motherfucker"


# the boc will do thefollowing:
# anything the user types after the "/" in the address bar it will be passed
# into the var called "name"
# the value of var "name" will be passed into the argument of the func called "user"
# this value gets passed into the "return" command and replaces every instance of {name}
# "f"Hello {name}!" is a format command which defines how the textis displayed
# e.g if the user types "127.0.0.1:5000/bitch"
# the "user" func will return "hello bitch"
@app.route("/<name>")
def user(name):
    return f"hello {name}"

# **********************************
# *       REDIRECT & URL_FOR       *
# **********************************
# the redirect & url_for modules are imported from the flask lib
# together when put inside a func with the return command it redirects 
# flask to another func found in another route
# this is normally used with a conditional statement which states if a condition
# is true return "page a" but if a condition is false redirect flask to another func
@app.route("/admin")
def admin():
    return redirect(url_for("holp"))


@app.route("/bitch")
def holp():
    return "<h1>you trying to go to the admin page motherfucker</h1>"











if __name__ == "__main__":
    app.run(debug=True)