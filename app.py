# app.py
from flask import Flask, g, render_template
import sqlite3

DATABASE = 'database.db'

# Initialize the Flask application
app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def home():
    #home page- just the ID, Maker, Model and Image URL
    sql = """
    SELECT MtBikeID, Makers.Name AS Maker, [Mt. Bike].Model, [Mt. Bike].ImageURL 
    FROM [Mt. Bike]
    JOIN Makers ON Makers.MakerID =[Mt. Bike].MakerID;
    """
    results = query_db(sql)
    return render_template('home.html', title='Home', MtBikes=results)

@app.route("/bike/<int:id>")
def bike(id):
    #just one bike based on the id
    sql = """
 SELECT [Mt. Bike].MtBikeID, Makers.Name AS Maker, [Mt. Bike].Model, [Mt. Bike].ImageURL, [Mt. Bike].Description, [Mt. Bike].Year, [Mt. Bike].Price
    FROM [Mt. Bike]
    JOIN Makers ON Makers.MakerID = [Mt. Bike].MakerID 
    WHERE [Mt. Bike].MtBikeID = ?;
    """
    result = query_db(sql, (id,), True)
    return render_template('bike.html', title='Bike Details', bike=result)



if __name__ == "__main__":
    app.run(debug=True)