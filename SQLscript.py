create_table_string = """CREATE TABLE IF NOT EXISTS logs(
                                id SERIAL PRIMARY KEY,
                                date_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP)"""

create_table_string = """CREATE TABLE IF NOT EXISTS rates(
                                log INTEGER NOT NULL,
                                date_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP)
                                first_curr VARCHAR(3) NOT NULL,
                                second_curr VARCHAR(3) NOT NULL,
                                rate DECIMAL NOT NULL,
                                colour CHAR(1) check(colour in ('G','R','W'))"""                                