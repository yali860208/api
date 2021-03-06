# -*- coding: UTF-8 -*-
import psycopg2
from app import db_config
import json

def sum_unblendedcost(usageaccountid):
    select_sum = '''SELECT product_productname, SUM(lineitem_unblendedcost) 
        FROM outputs
        WHERE lineitem_usageaccountid = '%s'
        GROUP BY product_productname;'''

    conn = None
    try:
        # read connection parameters
        params = db_config.config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        
        # create a cursor
        cur = conn.cursor()
        
        cur.execute(select_sum, (usageaccountid,))

        return_json = {}
        for i,j in cur.fetchall():
            return_json[i] = j

        # return result
        return return_json
        
    # close the communication with the PostgreSQL
        cur.close()

        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def sum_usageamount(usageaccountid):
    select_sum = '''SELECT product_productname,date_part('year',lineitem_usagestartdate) y,
       date_part('month',lineitem_usagestartdate) mon,
       date_part('day',lineitem_usagestartdate) d,
       SUM(lineitem_usageamount) FROM outputs WHERE lineitem_usageaccountid='%s'
       GROUP BY product_productname, y, mon, d ORDER BY product_productname, y, mon, d;'''

    conn = None
    try:
        # read connection parameters
        params = db_config.config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        
        # create a cursor
        cur = conn.cursor()
        
        cur.execute(select_sum, (usageaccountid,))

        return_json = {}
        sub_json = {}
        a = None
        for i,j,k,l,m in cur.fetchall():
            date = str(int(j)) + '-'+ str(int(k)) + '-'+ str(int(l))
            if a != i and a != None:
                sub_json = {}
            sub_json[date] = m
            return_json[i] = sub_json
            a = i
            
        return return_json
        
    # close the communication with the PostgreSQL
        cur.close()

        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def list_uid(pid):
    select_uid = '''SELECT lineitem_usageaccountid FROM outputs WHERE bill_payeraccountid='829432956742' GROUP BY bill_payeraccountid,lineitem_usageaccountid;'''

    conn = None
    try:
        # read connection parameters
        params = db_config.config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        
        # create a cursor
        cur = conn.cursor()

        cur.execute(select_uid, (pid,))
        return_json = {}
        for ind,i in enumerate(cur.fetchall()):
            return_json[ind+1] = i[0]
            
        return return_json
        
    # close the communication with the PostgreSQL
        cur.close()

        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def sum_usagecount(usageaccountid):
    select_sum = '''SELECT product_productname, 
        COUNT(product_productname) FROM outputs  
        WHERE lineitem_usageaccountid='%s'
         GROUP BY product_productname;'''

    conn = None
    try:
        # read connection parameters
        params = db_config.config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        
        # create a cursor
        cur = conn.cursor()
        
        cur.execute(select_sum, (usageaccountid,))

        return_json = {}
        for i,j in cur.fetchall():
            return_json[i] = j
            
        return return_json
        
    # close the communication with the PostgreSQL
        cur.close()

        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')