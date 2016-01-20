# -*- coding: utf-8 -*-

import sqlite3



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

def create_customer_table():
    sql = """CREATE TABLE Customer
            (CustomerID INTEGER,
            FirstName TEXT,
            LastName TEXT,
            Street TEXT,
            Town TEXT,
            PostCode INTEGER,
            TelephoneNumber INTEGER,
            EMailAddress TEXT,
            PRIMARY KEY(CustomerID))"""
    create_table(db_name, "Customer", sql)

def customer_order_table():
    sql = """CREATE TABLE CustomerOrder
            (OrderID INTEGER,
            Date TEXT,
            Time TEXT,
            CustomerID INTEGER,
            PRIMARY KEY(OrderID)
            FOREIGN KEY(CustomerID) references Customer(CustomerID)"""
    create_table(db_name, "CustomerOrder", sql)

def customer_order_table():
    sql = """CREATE TABLE OrderItem
            (OrderItemID INTEGER,
            OrderID INTEGER,
            ProductID INTEGER,
            Quantity INTEGER,
            PRIMARY KEY(OrderItemID)
            FOREIGN KEY(OrderID) references CustomerOrder(OrderID)
            FOREIGN KEY(ProductID) references Product(ProductID"""
    create_table(db_name, "CustomerOrder", sql)

def create_product_table():
    sql = """CREATE TABLE Product
            (ProductID INTEGER,
            Name TEXT,
            Price REAL,
            ProductTypeID INTEGER,
            PRIMARY KEY(ProductID)
            FOREIGN KEY(ProductTypeID) references ProductType(ProductTypeID)"""
    create_table(db_name, "Product", sql)


def create_product_type_table():
    sql = """CREATE TABLE ProductType
            (ProductTypeID INTEGER,
            Description TEXT,
            PRIMARY KEY(ProductTypeID))"""
    create_table(db_name, "ProductType", sql)

if __name__ == "__main__":
    db_name = "database.db"
    create_product_table()
    create_product_type_table()
