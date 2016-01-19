# -*- coding: utf-8 -*-

import sqlite3
db_name = "database.db"

sql = """CREATE TABLE Product
            (ProductID INTEGER,
            Name TEXT,
            Price REAL,
            PRIMARY KEY(ProductID))"""
            
def create_table(db_name, table_name, sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("SELECT NAME FROM SQLITE_MASTER WHERE NAME=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to recreate it(y/n): ".format(table_name))
            if response == "y":
                keep_table = False
                print("The {0} table will be recreated - all existing data will be lost".format(table_name,))
                cursor.execute("DROP TABLE IF EXISTS {0}".format(table_name))
                db.commit()
            else:
                print("The existing table was kept")
        else:
            keep_table = False
            
        if not keep_table:
            cursor.execute(sql)
            db.commit()
        
if __name__ == "__main__":
    create_table(db_name, "Product", sql)