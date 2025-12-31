from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/api/health")
def health():
    return {"status": "Backend is healthy"}

@app.route("/api/db")
def db_check():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("DB_PORT")
)
    return {"db": "connected successfully"}

app.run(host="0.0.0.0", port=5000)
