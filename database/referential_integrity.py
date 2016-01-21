import sqlite3

def query(sql, data):
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        #cursor.execute("PRAGMA FOREIGN_KEYS = ON")
        cursor.execute(sql,data)
        db.commit()
def update_producttype_id(new, old):
    sql = "UPDATE ProductType SET ProductTypeID=? WHERE ProductTypeID=?"
    query(sql,(new,old))
def update_customer_data(CustomerID,FirstName,LastName,Street,Town,PostCode,TelephoneNumber,EMailAddress):
    sql = ("UPDATE Customer SET FirstName=? WHERE CustomerID=?")
    query(sql,(FirstName,CustomerID))
    sql = ("UPDATE Customer SET LastName=? WHERE CustomerID=?")
    query(sql,(LastName,CustomerID))
    sql = ("UPDATE Customer SET Street=? WHERE CustomerID=?")
    query(sql,(Street,CustomerID))
    sql = ("UPDATE Customer SET Town=? WHERE CustomerID=?")
    query(sql,(Town,CustomerID))
    sql = ("UPDATE Customer SET PostCode=? WHERE CustomerID=?")
    query(sql,(PostCode,CustomerID))
    sql = ("UPDATE Customer SET TelephoneNumber=? WHERE CustomerID=?)
    query(sql,(TelephoneNumber,CustomerID))
    sql = ("UPDATE Customer SET EMailAddress=? WHERE CustomerID=?")
    query(sql,(EMailAddress,CustomerID)


if __name__ == '__main__':
    update_customer_data(1,"Antonio","Hallman","Den tredje lusvägen","Ottawa",9321,"0921853769122","gröntröja@bing.net")
