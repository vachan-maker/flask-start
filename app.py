from flask import Flask, render_template,request,redirect,url_for;

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login',methods=["POST", "GET"])
def login():
    if(request.method == "POST"):
        userName = request.form["nm"]
        return redirect(url_for("user",user=userName))
    else:
        return render_template("login.html")

@app.route("/<user>")
def user(user):
    return f"<h1>{user}</h1>"
if __name__ == "__main__":
    app.run(debug=True)