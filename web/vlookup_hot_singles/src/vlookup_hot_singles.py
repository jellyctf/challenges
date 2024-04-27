#!/usr/bin/env python3
from io import BytesIO
from flask import Flask, request, send_file, redirect, flash, url_for
from openpyxl import load_workbook

app = Flask(__name__)
# keep requests in memory 
# https://stackoverflow.com/a/28322143
# https://github.com/pallets/werkzeug/blob/2bcb43c3574de33b36174c6dc964182ccbc14a69/src/werkzeug/formparser.py#L59
app.config["MAX_CONTENT_LENGTH"] = 1024 * 500
app.config["SECRET_KEY"] = "shoh5keiBeo8PooW4gahZiu3ohthaiSh3phah@f-u2ohH7keiy0chu1cu2AhkeiT"

@app.route("/")
def index():
    return """
        <div>please upload a spreadsheet to populate with mutually beneficial partner candidates:</div>
        <form action="/spreadsheet" method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="upload">
        </form>
    """

@app.route("/spreadsheet", methods=["POST"])
def spreadsheet():
    if "file" not in request.files:
        flash("No file")
        return redirect(url_for("index"))
    file = request.files["file"]
    if file.filename == "":
        flash("No file")
        return redirect(url_for("index"))
    if file:
        wb = load_workbook(filename=file)
        ws = wb.active
        ws.append(["Username", "Email", "Socials", "Real Name", "Age", "Height", "Country", "MBTI", "Job", "Income", "Relationship status", "Favorite Sanrio Character", "Favorite Minecraft Version"])
        resp_sheet = BytesIO()
        wb.save(resp_sheet)
        resp_sheet.seek(0)
        flash("Your location has been recorded.")
        return send_file(
            resp_sheet,
            download_name="mutually_beneficial_partners.xlsx",
            as_attachment=True,
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)