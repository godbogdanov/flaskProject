import sqlite3
from flask import Flask, request, render_template, url_for, flash, redirect
from bs4 import BeautifulSoup, Tag
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Marking for inventory organization'
@app.route("/", methods=["GET","POST"])
def viewpackages():
    tagname = '<th>'
    tagname2 = '</th>'
    con = sqlite3.connect('2018_29_Адм_Петроградского_Богданов.sqlite3')
    con.row_factory = sqlite3.Row
    db = con.cursor()
    res = db.execute('select * from organization').fetchall()
    # if request.form:
    #     tagname = "<td><textarea>"
    #     tagname2 = "</td></textarea>"
    # return render_template("index.html", content=tagname, content2=tagname2, items=res)
    return render_template("index.html", items=res)

if __name__ == "__main__":
    app.run(debug=True)
