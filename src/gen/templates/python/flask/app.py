from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    # Renders the index.html file from the templates folder
    return render_template("index.html")


if __name__ == "__main__":
    # Starts the local development server (debug=True for automatic reloads)
    app.run(debug=True)
