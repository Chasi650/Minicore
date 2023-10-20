from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:udla1@localhost/minicore'  # Cambia estos valores según tu configuración
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))


class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idusuario = db.Column(db.Integer, db.ForeignKey('user.id'))
    fecha = db.Column(db.Date)
    monto = db.Column(db.Float)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
