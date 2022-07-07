db = {'host': 'localhost',
      'dbname': 'postgres',
      'password': 'postgres',
      'user': 'postgres',
      'port': 5432}

create_table_string = """CREATE TABLE IF NOT EXISTS rates(
                                id SERIAL PRIMARY KEY,
                                datetime TIMESTAMP NOT NULL,
                                curr1 VARCHAR(3) NOT NULL,
                                curr2 VARCHAR(3) NOT NULL,
                                rate DECIMAL NOT NULL,
                                colour VARCHAR(5) check(colour in ('green','red','white')) NOT NULL)"""

query_history = """SELECT datetime, curr1, curr2, rate, colour FROM rates"""

insert_into_tables_values = """INSERT INTO rates
                               (datetime, curr1, curr2, rate, colour)
                               VALUES (%s, %s, %s, %s, %s)"""