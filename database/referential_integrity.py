import sqlite3

def query(sql, data):
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA FOREIGN_KEYS = ON")
        cursor.execute(sql,data)
        db.commit()

if __name__ == '__main__':
    sql = "UPDATE ProductType set ProductTypeID = 57 WHERE ProductTypeID = 1"
    sql = "DELETE FROM ProductType WHERE ProductTypeID = 57"
    query(sql,())
