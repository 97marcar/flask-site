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

if __name__ == '__main__':
    update_producttype_id(1,2)
