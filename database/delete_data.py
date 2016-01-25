# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 15:00:13 2016

@author: 97marcar
"""

import sqlite3

def delete_product(data):
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        sql = "DELETE FROM Product WHERE ProductID=?"
        cursor.execute(sql,(data,))
        db.commit()

def delete_customer(data):
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        sql = "DELETE FROM Customer WHERE CustomerID=?"
        cursor.execute(sql,(data,))
        db.commit()

def delete_order(data):
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        sql = "DELETE FROM CustomerOrder WHERE OrderID=?"
        cursor.execute(sql,(data,))
        db.commit()

def delete_product_type(data):
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        sql = "DELETE FROM ProductType WHERE Description=?"
        cursor.execute(sql,(data,))
        db.commit()

def run_delete(type_to_del, data):
    if type_to_del == "product":
        delete_product(data)
    elif type_to_del == "customer":
        delete_customer(data)
    elif type_to_del == "customerorder":
        delete_order(data)
    elif type_to_del == "producttype":
        delete_product_type(data)
