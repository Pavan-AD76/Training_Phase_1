
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='18A23a12n2004@Nithya',
        database='customer'
    )
    return connection

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/report")
def report():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute('Select * from shopping_data')
    rows = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return render_template('report.html',rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
