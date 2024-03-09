# Yoinked from: https://realpython.com/python-web-applications/
from flask import Flask
from flask import request, escape
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    user_input = escape(request.args.get("user_input", ""))

    if user_input:
        try:
            result = subprocess.check_output("python3 ./awafier.py " + user_input, shell=True)
            result = result.decode()
        except:
            result = "Error processing input"
    else:
        result = ""

    return (
        """<h1>AWA5.0 Name converter</h1>"""
        + """<h3>Enter your name to generate an AWASCII script that prints out your name!</h3>"""
        + """<form action="" method="get">
                Enter your name here! <input type="text" name="user_input">
                <input type="submit" value="Convert to AWA5.0">
            </form>"""
        + "Awawawafied result:"
        + "<br/>"
        + '<span style="white-space: pre-line">' + result + '</span>'
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
