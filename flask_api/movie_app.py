from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import json

app = Flask(__name__)
mysql = MySQL(app)
app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "my-secret-pw"
app.config["MYSQL_DB"] = "movie_db"

def with_connection(func):
    def with_connection_(*args, **kwargs):
        con = mysql.connection
        result = func(*args, con=con, **kwargs)
        con.commit()
        con.close
        return result
    return with_connection_

@with_connection       
def create_row(table, str_row, con):                                    # str_row (string of VALUES with commas)
    cursor = con.cursor()
    insert_string = f"INSERT INTO {table} VALUES{str_row}"
    cursor.execute(insert_string)
    cursor.close()

@with_connection    
def retrieve_all_contents(table_name, con):
    cursor = con.cursor()
    query_string = f"SELECT * FROM {table_name}"
    cursor.execute(query_string)
    data = cursor.fetchall()                                            # json format
    cursor.close()
    return data                                                         # json good for api

@with_connection
@app.route("/")
def list_movie_table():
    movies_data = retrieve_all_contents("movies_tbl")
    movie_count = len(movies_data)
    return render_template("index.html", movies_data=movies_data, movie_count=movie_count)         #standard module, no installation required

@with_connection
@app.route("/new-movie")
def create_new_movie():
    tables = ["movies_tbl", "directors_tbl", "main_actors_tbl"]
    movies_data, directors_data, actors_data = (retrieve_all_contents(table) for table in tables)
    return render_template("new_movie.html", movies_data=movies_data, directors_data=directors_data, actors_data=actors_data)           

@with_connection
@app.route("/add-movie", methods=['POST'])
def add_new_movie():
    # from the form
    title = request.form['movie_title']                                   #json as well?
    release_year = request.form['release_year']
    director = request.form['director']

    # insert in movies_tbl
    movies_val = f'(null, "{title}", {release_year}, {director})'
    create_row("movies_tbl", movies_val)

    #insert main_actors
    last_movie_id = retrieve_all_contents("movies_tbl")[-1][0]
    actor_id = request.form['actor']
    actors_val = f"({last_movie_id}, {actor_id})"
    create_row("movie_actors_tbl", actors_val)

    #go back to main page and view
    return redirect(url_for("list_movie_table"))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
    