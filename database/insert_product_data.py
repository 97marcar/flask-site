# -*- coding: utf-8 -*-

import sqlite3

def insert_data(values):
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        sql = "INSERT INTO Product (Name, Price) VALUES (?,?)"
        cursor.execute(sql,values)
        db.commit()
        
if __name__ == "__main__":
    product = ("Americano", 1.50)
    insert_data(product)