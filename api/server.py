from flask import Flask, jsonify, render_template
import pymongo
from config import MONGO_URI, DB_NAME, COLLECTION_NAME
from run_etl import run_etl

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/earthquakes")
def get_earthquakes():
    client = pymongo.MongoClient(MONGO_URI)
    db = client[DB_NAME]
    cursor = db[COLLECTION_NAME].find({}, {"_id": 0})
    data = list(cursor)
    client.close()
    return jsonify(data)

if __name__ == "__main__":
    run_etl()
    app.run(debug=True)
