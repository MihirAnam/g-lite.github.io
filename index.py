from flask import *
from assistant import *

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def register():
    return render_template("index.html")


@app.route("/search",methods=['post'])
def search():
    query1=request.form['search']
    ans1=query(query1)
    search.ans1=ans1
    return render_template("index.html",answer1=ans1,question=query1)



@app.route("/ask",methods=['post'])
def search1():
    query2=ask()
    if query2=="novoice":
        return render_template("index.html")
    else:
        ans2=query(query2)
        return render_template("index.html",answer1=ans2,question=query2)


if __name__ == "__main__":
    app.run(debug=True)
