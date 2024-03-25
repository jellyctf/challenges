#!/usr/bin/env python3
from flask import Flask, request, redirect, flash, url_for
from openpyxl import load_workbook

app = Flask(__name__)

@app.route("/")
def index():
    return """
        <div>please upload the spreadsheet of mutually beneficial partner candidates:</div>
        <form action="/spreadsheet" method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="upload">
        </form>
    """

@app.route("/spreadsheet", methods=['POST'])
def spreadsheet():
    wb = load_workbook(filename='example.xlsx')
    ws = wb.active
    ws['A1'] = 42
    ws.append([1, 2, 3])
    wb.save("example.xlsx")
    return "Your location has been recorded."

    if 'file' not in request.files:
        flash('No file')
        return redirect(url_for('index'))
    file = request.files['file']
    if file.filename == '':
        flash('No file')
        return redirect(url_for('index'))
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)