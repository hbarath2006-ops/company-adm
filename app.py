db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="barath8114@#f",
    database="company_portal"
)
import os

db = mysql.connector.connect(
    host=os.environ.get("DB_HOST"),
    port=int(os.environ.get("DB_PORT")),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    database=os.environ.get("DB_NAME")
)
