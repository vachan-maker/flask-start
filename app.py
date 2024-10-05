from flask import Flask, render_template,request,redirect,url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/postOffice", methods=["POST", "GET"])
def postOffice():
    if(request.method == "POST"):
        pinCode = request.form["pincode"]
        return redirect(url_for("pinCodeInfo", pinCode = pinCode))
    else:
        return render_template("postOffice.html")
    
@app.route("/postOffice/<pinCode>")
def pinCodeInfo(pinCode):
    response = requests.get(f"https://api.postalpincode.in/pincode/{pinCode}")
    if response.status_code == 200:
        details = response.json()
        postOfficeName = details[0]['PostOffice'][0]['Name']
        return render_template("pinCode.html",poName = postOfficeName)
    else:
        return "Error - No Data Found!"


if __name__ == "__main__":
    app.run(debug=True)


# @app.route('/login',methods=["POST", "GET"])
# def login():
#     if(request.method == "POST"):
#         userName = request.form["nm"]
#         return redirect(url_for("user",user=userName))
#     else:
#         return render_template("login.html")
    

# @app.route("/user/<user>")
# def user(user):
#     return f"<h1>{user}</h1>"


