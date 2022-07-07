import psycopg2
import SQLscript

def connect_to_db():
    connection = psycopg2.connect(**SQLscript.db)
    cursor = connection.cursor()
    return connection, cursor

def create_table(cursor):
    cursor.execute(SQLscript.create_table_string)    

def close_connection(connection, cursor):
    cursor.close()
    connection.close()

def parse_data(obj, cursor, connection):
    cursor.execute(SQLscript.insert_into_tables_values, obj.attributes())
    connection.commit()

def history(cursor):
    cursor.execute(SQLscript.query_history)
    rates = cursor.fetchall()  
    return rates 