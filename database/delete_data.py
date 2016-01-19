# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 15:00:13 2016

@author: 97marcar
"""

import sqlite3

def delete_product(data):
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        sql = "DELETE FROM Product WHERE Name=?"
        cursor.execute(sql,data)
        db.commit()
        
if __name__ == "__main__":
    data = ("Tea",)
    delete_product(data)