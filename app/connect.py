import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def create_tables():
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        cur.execute('''
            CREATE TABLE outputs (
            id SERIAL,
            bill_PayerAccountId varchar NOT NULL,
            lineItem_UnblendedCost real NOT NULL,
            lineItem_UnblendedRate real,
            lineItem_UsageAccountId varchar NOT NULL,
            lineItem_UsageAmount real NOT NULL,
            lineItem_UsageStartDate timestamp NOT NULL,
            lineItem_UsageEndDate timestamp NOT NULL,
            product_ProductName varchar NOT NULL
            )''')

        cur.execute('''
            COPY outputs
            FROM 'app/data.csv'
            DELIMITER ','
            CSV HEADER''')
        print('copy success')
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    connect()
    create_tables()