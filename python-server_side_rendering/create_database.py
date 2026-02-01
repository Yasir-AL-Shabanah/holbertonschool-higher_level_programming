import sqlite3


def create_database():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
        """
    )
    # تنظيف البيانات القديمة (لو السكربت انعاد تشغيله)
    cursor.execute("DELETE FROM Products")
    cursor.execute(
        """
        INSERT INTO Products (id, name, category, price)
        VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        """
    )
    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_database()
