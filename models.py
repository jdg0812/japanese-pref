from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Japan(db.Model):
    id = db.Column(db.String(5), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    have_been = db.Column(db.String(3), nullable=False)
    date = db.Column(db.Date, nullable=True)

    def to_json(self):
        return {
            "id": self.id, 
            "name": self.name,
            "have_been": self.have_been,
            "date": self.date,
        }
 