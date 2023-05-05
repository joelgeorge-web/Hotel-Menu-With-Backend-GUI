from flask import Flask, render_template, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/db'
db = SQLAlchemy(app)

class SelectedData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id1 = db.Column(db.Integer, default=0)
    id2 = db.Column(db.Integer, default=0)
    id3 = db.Column(db.Integer, default=0)
    id4 = db.Column(db.Integer, default=0)
    id5 = db.Column(db.Integer, default=0)
    id6 = db.Column(db.Integer, default=0)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/save', methods=['POST'])
def save():
    data = {}
    for i in range(1, 7):
        data[f'id{i}'] = request.form[f'data{i}']
    selected_data = SelectedData(**data)
    db.session.add(selected_data)
    db.session.commit()
    return 'Confirmed successfully!'

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run()
