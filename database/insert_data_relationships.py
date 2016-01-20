# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 19:06:08 2016

@author: marcus
"""

import sqlite3

def query(sql, data):
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        cursor.execute(sql,data)
        db.commit()

def insert_product_type_data(records):
    sql = "INSERT INTO ProductType(Description) VALUES (?)"
    for record in records:
        print(record)
        query(sql, record)

def insert_product_data(records):
    sql = "INSERT INTO Product (Name,Price,ProductTypeID) VALUES (?,?,?)"
    for record in records:
        print(record)
        query(sql,record)

def insert_customer_data(records):
    sql = "INSERT INTO Customer(FirstName,LastName,Street,Town,PostCode,TelephoneNumber, \
    EMailAddress)VALUES (?,?,?,?,?,?)"
    for record in records:
        print(record)
        query(sql,record)

def insert_order_data(records):
    sql = "INSERT INTO CustomerOrder(OrderID,CustomerID, Date, Time)VALUES (?,?)"
    for record in records:
        print(record)
        query(sql,record)

if __name__ == "__main__":
    product_types = [("Coffee",),("Tea",),("Soda",)]
    insert_product_type_data(product_types)
    products = [("Latte", 1.35, 1),("Mocha", 2.40, 1),("Green Tea", 1.20, 2),
    ("Black Tea", 1.00, 2),("Americano", 1.50, 3),("Raspberry", 3.50, 3),("Lemonade",2.85,3)]
    insert_product_data(products)
