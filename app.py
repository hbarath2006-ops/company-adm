from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)

app.secret_key = "change_this_secret_key"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="barath8114@#",
    database="company_portal"
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():

    email = request.form["email"]
    password = request.form["password"]

    cursor = db.cursor(dictionary=True)

    query = """
    SELECT * FROM users
    WHERE email = %s AND password = %s
    """

    cursor.execute(query, (email, password))

    user = cursor.fetchone()

    cursor.close()

    if user:
        session["email"] = user["email"]
        return redirect("/dashboard")

    return redirect("/")


@app.route("/dashboard")
def dashboard():

    if "email" not in session:
        return redirect("/")

    return render_template(
        "dashboard.html",
        email=session["email"]
    )


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)