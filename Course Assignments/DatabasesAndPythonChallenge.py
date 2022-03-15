import sqlite3
from sqlite3 import Error

def create_connection():
    """create a database connection to a SQLite database that resides
        in the memory
    """
    conn = None
    try:
        conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


# projects table
CREATE TABLE IF NOT EXISTS projects (
	id integer PRIMARY KEY,
	name text NOT NULL,
	begin_date text,
	end_date text
);

# tasks table
CREATE TABLE IF NOT EXISTS tasks (
	id integer PRIMARY KEY,
	name text NOT NULL,
	priority integer,
	project_id integer NOT NULL,
	status_id integer NOT NULL,
	begin_date text NOT NULL,
	end_date text NOT NULL,
	FOREIGN KEY (project_id) REFERENCES projects (id)
);






if __name__ == '__main__':
    create_connection()



