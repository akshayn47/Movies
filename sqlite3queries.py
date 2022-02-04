import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_movie(conn, movies):
    """
    insert a new movie
    :param conn:
    :param movie:
    :return:
    """

    sql = ''' INSERT INTO Movies(name,actor,actress,director,yearofrelease)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, movies)
    conn.commit()

def select_all_movies(conn):
    """
    Query all rows in the movies table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Movies")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_movie_by_actor(conn, actorr):
    """
    Query movies by actor name
    :param conn: the Connection object
    :param actor:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Movies WHERE actor=?", (actorr,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    database = r"D:\sqlite3\db\pythonsqlite.db"

    sql_create_movies_table = """ CREATE TABLE IF NOT EXISTS Movies (
                                        name text PRIMARY KEY,
                                        actor text NOT NULL,
                                        actress text NOT NULL,
                                        director text NOT NULL,
                                        yearofrelease integer
                                        ); """

    

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_movies_table)
        print("Enter no of records to be inserted:")
        n=int(input())
        for i in range(n):
            print("Enter a movie name:")
            name=input()
            print("Enter actor name:")
            actor=input()
            print("Enter actress name:")
            actress=input()
            print("Enter director name:")
            director=input()
            print("Enter Year of Release:")
            yrofrelease=int(input())
            movies=(name,actor,actress,director,yrofrelease)
            insert_movie(conn,movies)

        print("Query all movies:")
        select_all_movies(conn)
        print("Enter actor name to search:")
        actorr=input()
        print("Query movie by actor:")
        select_movie_by_actor(conn, actorr)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()