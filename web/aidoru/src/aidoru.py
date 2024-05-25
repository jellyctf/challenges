from flask import Flask
from flask import render_template
from app_secrets import get_uuid
import json

app = Flask(__name__)

# Public visibility true/false
TALENTS = {
    "rie": True,
    "panko": True,
    "lumi": True,
    "jelly": False,
    "uruka": True,
    "lia": True
}

def get_profile(name):
    if name not in TALENTS.keys() or not TALENTS[name]:
        return "/404"
    return "/covers/" + str(get_uuid(name))

@app.route('/404')
def page_not_found():
    return ("""<h1>Page not found</h1>"""
            + "The idol page you requested may be unpublished or does not exist.\n"
            + "<div><img src=static/404.gif></div>")

@app.route('/covers/<uuid>')
def covers(uuid):
    with open('static/secret_data/' + f"{uuid}.json", 'r') as f:
        json_data = json.load(f)

    return render_template("profile.html", data=json_data)

@app.route("/")
def index():
    return render_template("index.html", len = len(list(TALENTS.keys())), talents = list(TALENTS.keys()))

app.jinja_env.globals.update(get_profile=get_profile)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
