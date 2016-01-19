# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 14:56:28 2016

@author: 97marcar
"""

import sqlite3

def update_product(data):
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        sql = "UPDATE Product SET Name=?, Price=? WHERE ProductID=?"
        cursor.execute(sql,data)
        db.commit()
        
if __name__ == "__main__":
    data = ("Latte", 2.45, 1)
    update_product(data)