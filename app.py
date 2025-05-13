from flask import Flask ,redirect,url_for
app = Flask(__name__) 


#CREATING WEB PAGES

@app.route("/")
def home():
    return "Hello! This is the Main Page <h1>HELLO</h1>" 



#DYNAMIC PAGE
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


#REDIRECTS
@app.route("/admin")
def admin():
    return redirect(url_for("home"))



# This runs the app only if this file is run directly (not imported as a module)
if __name__=="__main__":
    app.run(debug=True) #Starts server locally on 127.0.0.1:5000