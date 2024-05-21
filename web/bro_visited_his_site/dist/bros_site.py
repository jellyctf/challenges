#!/usr/bin/env python3
from flask import Flask, request, render_template_string, send_from_directory

app = Flask(__name__)
app.config["FLAG"] = "jellyCTF{redacted}"

@app.route("/")
def index():
    return """
        <img src="/static/bro.jpg" />
        <form action="/response" method="get">
            <textarea cols="50" name="word"></textarea>
            <input type="submit" value="go">
        </form>
    """

@app.route("/response")
def response():
    word = request.args.get("word", "")

    return render_template_string(f'''
        {{% set config="friend" %}}
        {{% set self="visit" %}}
        <p>
            {word}pilled {word}maxxer
        </p>
    ''')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)