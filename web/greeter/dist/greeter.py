#!/usr/bin/env python3
from flask import Flask, request, render_template_string

app = Flask(__name__)
app.config["FLAG"] = "redacted"

@app.route("/")
def index():
    return """
        <div>hi, what's your name</div>
        <form action="/hello" method="get">
            <input type="text" name="name">
            <input type="submit" value="go">
        </form>
    """

@app.route("/hello")
def hello():
    name = request.args.get("name", "")

    return render_template_string('''
        {{% set config="that name SUCKS" %}}
        {{% set self="that name SUCKS" %}}
        <p>
            hello {}
        </p>
    '''.format(name))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
