#!/usr/bin/env python3
from flask import Flask, request, render_template_string
from openpyxl import load_workbook

app = Flask(__name__)

@app.route("/")
def index():
    return """
        
    """

@app.route("/spreadsheet")
def spreadsheet():
    wb = load_workbook(filename='example.xlsx')
    ws = wb.active
    ws['A1'] = 42
    ws.append([1, 2, 3])
    wb.save("example.xlsx")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)