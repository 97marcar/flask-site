# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 15:36:51 2016

@author: 97marcar
"""

import sqlite3
import select_existing_products
import insert_product_data
import delete_data
import create_product_table
import update_data

def ui():
    print("1. (Re)Create Product Table")
    print("2. Add new product")
    print("3. Edit existing product")
    print("4. Delete existing product")
    print("5. Search Product")
    print("0. Exit")
    
    choice = input("Choose option: ")
    if choice == "1" or choice == 1:
        create_product_table.create_table(create_product_table.db_name, "Product", create_product_table.sql)
        ui()
    elif choice == "2" or choice == 2:
        inserted_name = input("Name product: ")
        inserted_price = float(input("Price: "))
        values_to_insert = (inserted_name, inserted_price)
        insert_product_data.insert_data(values_to_insert)
        ui()
    elif choice == "3" or choice == 3:
        updated_name = input("New Name: ")
        updated_price = float(input("New Price: "))
        id_where_updated = int(input("Choose which ID that will be updated: "))
        tuple_to_be_used_to_update = (updated_name,updated_price,id_where_updated)
        update_data.update_product(tuple_to_be_used_to_update)
        ui()
    elif choice == "4" or choice == 4:
        deleted_name = input("Name of Product to be deleted: ")
        delete = (deleted_name,)
        delete_data.delete_product(delete)
        ui()
    elif choice == "5" or choice == 5:
        selected_id = int(input("Enter ID of the item you wish to select: "))
        select_existing_products.select_product(selected_id)
        ui()
    else:
        print("exit.")


if __name__ == "__main__":
    ui()