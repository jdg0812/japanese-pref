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
 

# import pandas as pd

# df = pd.read_excel('Untitled spreadsheet.xlsx')
# with app.app_context():
#     db.session.query(Japan).delete()
#     prefectures = []  # Initialize an empty list

#     for index, row in df.iterrows():
#         prefectures.append({
#             "id": row["ID"],
#             "name": row["TITLE"],
#             "have_been": row["HAVE_BEEN"],
#         })

#     print(prefectures)

#     for p in prefectures:
#         new_prefecture = Japan(id=p["id"], name=p["name"], have_been=p["have_been"])
#         db.session.add(new_prefecture)
    
#     db.session.commit()  # Save changes