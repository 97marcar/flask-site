# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 19:06:08 2016

@author: marcus
"""

import sqlite3
import time

abc =(time.strftime("%H:%M:%S")) #local time
abd =(time.strftime("%d/%m/%Y")) #local date
#for some reason the names time =.. and date =.. did not work

print(abd)

def query(sql, data):
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        cursor.execute(sql,data)
        db.commit()

def insert_product_type_data(description):
    sql = "INSERT INTO ProductType (Description) VALUES (?)"
    query(sql, description)

def insert_product_data(records):
    sql = "INSERT INTO Product (Name,Price,ProductTypeID) VALUES (?,?,?)"
    print(records)
    query(sql,records)

def insert_customer_data(records):
    sql = "INSERT INTO Customer(FirstName,LastName,Street,Town,PostCode,TelephoneNumber, \
    EMailAddress)VALUES (?,?,?,?,?,?,?)"
    print(records)
    query(sql,records)

def insert_order_customer_data(records):
    sql = "INSERT INTO CustomerOrder(Date, Time, CustomerID, Quantity) VALUES (?,?,?,?)"
    query(sql,(records))

# def insert_order_item_data(records):
#    sql = "INSERT INTO OrderItem(OrderID,ProductID,Quantity) VALUES (?,?,?)"
#    for record in records:
#        print(record)
#        query(sql, record)
if __name__ == '__main__':
    insert_product_type_data(("test",))
#if __name__ == "__main__":
#    product_types = [("Coffee",)]
#    products = [("Latte", 1.35, 1)]
#    customer_data = [("Anton","Hallman","Den tredje lusvägen","Ottawa",9321,"0921853769122","swag@bing.net")]
#    customer_order = [(abc,abd,1)]
#    order_item = [(1,1,1)]
#    insert_product_type_data(product_types)
#    insert_product_data(products)
#    insert_customer_data(customer_data)
#    insert_order_customer_data(customer_order)
#    insert_order_item_data(order_item)
