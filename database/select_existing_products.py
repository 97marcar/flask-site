# -*- coding: utf-8 -*-

import sqlite3

def select_all_products():
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Product")
        products = cursor.fetchall()
        return products
        
def select_product(id):
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT Name, Price FROM Product WHERE ProductID=?",(id,))
        product = cursor.fetchone()
        return product
        
if __name__ == "__main__":
    products = select_all_products()
    print(products)
    product = select_product(3)
    print(product)