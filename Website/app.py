from flask import Flask, render_template, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/db'
db = SQLAlchemy(app)

class SelectedData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data1 = db.Column(db.String(50))
    data2 = db.Column(db.String(50))
    data3 = db.Column(db.String(50))
    data4 = db.Column(db.String(50))
    data5 = db.Column(db.String(50))
    data6 = db.Column(db.String(50))

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/save', methods=['POST'])
def save():
    data1 = request.form['data1']
    data2 = request.form['data2']
    data3 = request.form['data3']
    data4 = request.form['data4']
    data5 = request.form['data5']
    data6 = request.form['data6']
    selected_data = SelectedData(data1=data1, data2=data2, data3=data3, data4=data4, data5=data5, data6=data6)
    db.session.add(selected_data)
    db.session.commit()
    return 'Confirm successfully!'

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run()
