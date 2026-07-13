from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/create-account")
def create_account():
    return render_template("create_account.html")
if __name__ == "__main__":
    app.run(debug=True)