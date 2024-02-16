from flask import Flask, url_for, redirect
import settings as stg



app = Flask(__name__, static_folder = stg.PATH_STATIC)
app.config["SECRET_KEY"] = stg.SECRET_KEY

@app.route("/")
def index():
    url = url_for("templates/index.html")
    return "ВОВА НЕГР"

@app.route("/post/category")
def post_category():
    return "ТУТ БУДЕ ОЛЕГ"

@app.route("/post/view")
def post_view():
    return "ТУТ ОЛЕГ"

@app.route("/about")
def about():
    return " ІНФОРМАЦІЯ ПРО ОЛЕГА"

app.run(debug=True)
