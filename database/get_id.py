import sqlite3

def select_product(email):
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT CustomerID FROM Customer WHERE EMailAddress=?",(email,))
        customer_id = cursor.fetchone()
        print (customer_id)
        return customer_id

if __name__ == '__main__':
    select_product("s")
