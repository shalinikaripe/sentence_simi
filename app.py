import opcode
from flask import Flask, render_template, request
import os
import difflib
app = Flask(__name__)
@app.route("/")
def FUN_root():
    return render_template("project2.html")
@app.route('/regact', methods=['POST', 'GET'])
def homepage():
    if request.method == 'POST':
        s1 = request.form['s1']
        s2 = request.form['s2']
        op=difflib.SequenceMatcher(None,s1,s2).ratio()
        op1=op*100
        return render_template('project2.html',op1=op1)
    else:
        return render_template('project2.html')
if __name__ == "__main__":
  app.run(port=8000, debug=True)
