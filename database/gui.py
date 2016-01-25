import sqlite3
import insert_data_relationships as insert
import referential_integrity as edit
import create_product_table as create
import get_id
import time
import delete_data as delete
import update_data as update

a_time =(time.strftime("%H:%M:%S")) #local time
a_date =(time.strftime("%d/%m/%Y")) #local date
#for some reason the names time =.. and date =.. did not work

quantity = 0

def gui():
    global quantity
    quantity = 0
    print("1. (Re)Create Product Table")
    print("2. Add a new product type")
    print("3. Make a new order")
    print("4. Delete something")
    print("5. Edit a product")
    print("0. Exit")
    choice = int(input("Choose option: "))

    if choice == 1:
        create.create_table_functions()
        gui()

    elif choice == 2:
        new_product_type = str(input("Name of the product type: "))
        insert.insert_product_type_data((new_product_type,))
        gui()

    elif choice == 3:
        print("1. Returning customer")
        print("2. New customer")
        new_customer = int(input("Choose option: "))

        if new_customer == 1:
            customer_id = str(input("Enter customer id: "))

        else:
            customer_firstname = str(input("Enter first name: "))
            customer_lastname = str(input("Enter last name: "))
            customer_street = str(input("Enter street: "))
            customer_town = str(input("Enter town: "))
            customer_postcode = str(input("Enter postcode: "))
            customer_phonenumber = str(input("Enter phone number: "))
            customer_email  = str(input("Enter email: "))
            print(customer_email)

            customer = (customer_firstname, customer_lastname, customer_street, \
            customer_town, customer_postcode, customer_phonenumber, customer_email)
            insert.insert_customer_data(customer)

            customer_id_temp = get_id.select_product(customer_email)
            customer_id = customer_id_temp[0]
            print(customer_id)


        product()
        insert.insert_order_customer_data((a_date, a_time, customer_id, quantity))
        print("done")
        gui()

    elif choice == 4:
        print("What would you like to delete?")
        print("1. A Product ")
        print("2. A Customer")
        print("3. A Order")
        print("4. A Product Type")
        delete_choose = int(input("Choose option: "))
        if delete_choose == 1:
            data = input("ProductID of item to be deleted: ")
            delete.run_delete("product", data)
        elif delete_choose == 2:
            data = input("CustomerID of customer to be deleted: ")
            delete.run_delete("customer", data)
        elif delete_choose == 3:
            data = input("OrderID of order to be deleted: ")
            delete.run_delete("customerorder", data)
        elif delete_choose == 4:
            data = input("Name of product type to be deleted: ")
            delete.run_delete("producttype", data)
        gui()

    elif choice == 5:
        product_to_edit_id = str(input("ProductID of product to edit: "))
        product_to_edit_name = str(input("New name: "))
        product_to_edit_price = float(input("New Price: "))
        update.update_product((product_to_edit_name, product_to_edit_price, product_to_edit_id))



def product():
    global quantity
    product_name = str(input("Name of product: "))
    product_price = float(input("Price of product: "))
    product_id = int(input("Which type of product?: "))
    product_info = (product_name, product_price, product_id )
    insert.insert_product_data(product_info)
    quantity += 1
    buy_more = str(input("Did the customer buy more?[y/n]: "))
    if buy_more == "y":
        product()


if __name__ == '__main__':
    gui()
