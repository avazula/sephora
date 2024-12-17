from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World"


@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if valid_login(request.form["username"], request.form["password"]):
            return redirect(url_for("home"))
        else:
            error = "Invalid username/password"
    return render_template("login.html", error=error)


def valid_login(username: str, password: str) -> bool:
    return username == "admin" and password == "admin"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
