# Yoinked from: https://realpython.com/python-web-applications/
from flask import Flask
from flask import request, escape
import subprocess
import awafier_decoder

app = Flask(__name__)

@app.route("/")
def index():
    user_input = escape(request.args.get("user_input", ""))

    if user_input:
        try:
            result = subprocess.check_output(['python3', './awafier_decoder.py', '{}'''.format(user_input)], stderr=subprocess.STDOUT)
            result = result.decode()
            print(result)
        except:
            result = "Invalid AWASCII - do better"
    else:
        result = ""

    return (
        """<h1>AWASCII validator</h1>"""
        + """<h3>Want to check if your AWASCII is valid? Enter it in this form to validate and decode it!</h3>"""
        + """<h3>Note: Reminder - AWASCII is 6 bits. A starting awa is required!</h3>"""
        + """<form action="" method="get">
                Enter your AWASCII here! <input type="text" name="user_input">
                <input type="submit" value="Decode AWASCII">
            </form>"""
        + "AWASCII decoded result:"
        + "<br/>"
        + '<span style="white-space: pre-line">' + result + '</span>'
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)