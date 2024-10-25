import sqlite3

#? A Simple Program Using SQLite to demonstrate it's usage


conn = sqlite3.connect("customer_data.db")
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS customers (name TEXT,age INT,email TEXT)")

def add_data():
    """Adds The Customer's Data In The Customers List
    """
    customers = []
    num_customers = int(input("Enter How Many Customers Records Will Be Put Into The Database : "))
    for _ in range(num_customers):
        Name = input("Enter The Name Of The Customer : ")
        Age = int(input("Enter The Age Of The Customer : "))
        Email = input("Enter The Email Of The Customer : ")
        customers.append((Name,Age,Email))
        print()
        print(f"Customer : {Name}'s Data Added In The Database!")
    c.executemany("INSERT INTO customers VALUES (?,?,?)",customers)
    conn.commit()
    print("Customer Data Added To The Database!")   
    

def show_customer_data():
    c.execute("SELECT rowid, * FROM customers")
    customer_data = c.fetchall()
    if customer_data:
        print("Customer Data In The Database \n")
        for customer in customer_data:
            print(f"ID : {customer[0]} |  NAME : {customer[1]} | AGE : {customer[2]} | EMAIL : {customer[3]}")
        print(f"\nShowed {len(customer_data)} results present in the Database!")
    else:
        print("No Records Present In The Database!")

def find_customer():
    search = int(input("Enter The ID Of The Customer You Want to Find : "))
    c.execute("SELECT rowid, * FROM customers WHERE rowid = ?",(search,))
    customer_data = c.fetchone()

    if customer_data:
        print("Customer Found!")
        print(f"NAME : {customer_data[1]} | AGE : {customer_data[2]} | EMAIL : {customer_data[3]}")
    else:
        print("Customer Not Found!")     

add_data()
print()
show_customer_data()
print()
find_customer()
    

conn.close()
