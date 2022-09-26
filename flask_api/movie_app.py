from flask import Flask, render_template
from flask_mysqldb import MySQL
import json

app = Flask(__name__)
mysql = MySQL(app)
app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "my-secret-pw"
app.config["MYSQL_DB"] = "movie_db"


@app.route("/")
def hello_world():
    return "<p>Hello World</p>"

@app.route("/movies/")
def list_movies():
    cursor = mysql.connection.cursor()
    query_string = "SELECT * FROM movies_tbl"
    cursor.execute(query_string)
    data = cursor.fetchall()                                        #json format
    cursor.close()
    return json.dumps(data)                                         # standard module, no installation required
# json good for api

@app.route("/movies-table/")
def list_movie_table():
    cursor = mysql.connection.cursor()
    query_string = "SELECT * FROM movies_tbl"
    cursor.execute(query_string)
    data = cursor.fetchall()                                        #json format
    cursor.close()
    return render_template("movies.html", movies_data=data)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)