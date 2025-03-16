from flask import Flask, request, jsonify, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from models import Japan, db, app
from datetime import datetime
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

@app.route('/')
def index():
    japan = Japan.query.all()
    visited = [row.id for row in japan if row.have_been == "YES"]
    id_title_map = {row.id: row.name for row in japan}
    return render_template('index.html', visited=visited, id_title_map=id_title_map, japan=japan)

@app.route('/get_japan', methods=['GET'])
def get_japan():
    japan = Japan.query.all()
    japan_json = list(map(lambda x: x.to_json(),japan))
    return jsonify({"transactions": japan_json})



@app.route('/update_japan/<string:id>', methods=['POST'])
def update_japan(id):
    prefecture = Japan.query.get(id)
    if not prefecture:
        return jsonify({"message": "Transaction not found"}), 404

    date_value = request.form['date']
    if date_value:
        prefecture.date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
    else:
        prefecture.date = None
    prefecture.have_been = request.form['have_been'].upper()
    

    try:
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return redirect("/#container")

# # Fetch Prefecture Data from DB
# def get_prefecture_data():
#     conn = db_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM japan")
#     rows = cur.fetchall()
#     conn.close()

#     # Extract visited prefectures & map ID to Name
#     visited = [row["ID"] for row in rows if row["HAVE_BEEN"] == "yes"]
#     id_title_map = {row["ID"]: row["TITLE"] for row in rows}

#     return visited, id_title_map

# @app.route('/')
# def index():

#     visited, id_title_map = get_prefecture_data()
#     return render_template('index.html', visited=visited, id_title_map=id_title_map)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
