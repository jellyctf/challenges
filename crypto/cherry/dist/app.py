from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('slots.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)