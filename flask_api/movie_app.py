from flask import Flask, render_template, request
from flask_mysqldb import MySQL

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

                                       
#DELETE FROM directors_tbl WHERE id=2;
@with_connection
@app.route("/")
def list_movie_table():
    movies_data = retrieve_all_contents("movies_tbl")
    return render_template("index.html", movies_data=movies_data)         #standard module, no installation required

@with_connection
@app.route("/new-movie")
def create_new_movie():
    tables = ["movies_tbl", "directors_tbl", "main_actors_tbl"]
    movies_data, directors_data, actors_data = (retrieve_all_contents(table) for table in tables)
    return render_template("new-movie.html", movies_data=movies_data, directors_data=directors_data, actors_data=actors_data)           

@with_connection
@app.route("/add-movie", methods=['POST'])
def add_new_movie():
    # from the form
    title = request.form['movie_title']                                   #json as well?
    release_year = request.form['release_year']
    director_id = request.form['director_id']

    #insert in movies_tbl
    movies_val = f"(null, {title}, {release_year}, {director_id})"
    create_row("movies_tbl", movies_val)

    #insert main_actors
    actors_val = f"(new_movie_id, actor_id)"
    create_row("main_actors_tbl", actors_val)

    return list_movie_table()

"""@with_connection
def update_table(con, table_name):
    return

@with_connection
def delete_table(con, table_name, condition):

@app.route('/movies/create')
def create():
    insert('movies_tbl', "(null, 'TalentAcademy', 2022, 3)")
    return json.dumps()         # should flash message that value was inserted

#@app.route('/movies/delete' , methods = ['GET','POST'])
#def delete():
#    cursor
"""

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
    