from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres156@localhost/height_collector'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__='data'
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(120), unique=True)
    height=db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_=email_
        self.height_=height_

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        email=request.form['email_name']
        height=request.form['height_name']
        print(email, height)
    return render_template('success.html')

if __name__ == "__main__":
    app.debug=True
    app.run()