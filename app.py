from flask import Markup
from flask import Flask,Response, request
from flask import render_template
from  index import main

app = Flask(__name__)

@app.route("/") 
def chart():
    baz = main() 
    labels = [0,2,4,6,8,10]
    values = baz
    return render_template('chart.html', values=values, labels=labels)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)