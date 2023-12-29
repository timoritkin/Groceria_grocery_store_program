import hashlib
import os
from tkinter import messagebox
import mysql.connector


def initialize_connection():
    conn = mysql.connector.connect(
        host='localhost',

        user='root',
        password='123456',
        database='mini_market_db'
    )
    # cur == cur
    cursor = conn.cursor()

    return conn, cursor


def login(cur, conn, phone_number, password):
    # query = """SELECT customer_id, first_name, last_name
    #            FROM customer
    #            WHERE phone_number = %s """
    #
    # cur.execute(query, phone_number)
    # result = cur.fetchone()

    query = """SELECT cust_password, security_salt, customer_id, first_name, last_name
               FROM customer
               WHERE phone_number = %s """

    cur.execute(query, (phone_number,))
    result = cur.fetchone()

    print(type(result[0]), type(result[1]))
    if result is not None and verify_password(result[0], password, result[1]):

        user_id = result[2]
        first_name = result[3]
        last_name = result[4]

        # Create a new order for the logged-in user
        create_order_query = """INSERT INTO my_order (order_date, total_price,
         Customer_customer_id, shipment_id, payment_id)
                                VALUES (NOW(), 0.0, %s, NULL, NULL)"""
        cur.execute(create_order_query, (user_id,))
        conn.commit()

        # Get the last inserted order_id
        order_id = cur.lastrowid

        # Now we can use the order_id for the user's current order

        return user_id, order_id, first_name, last_name
    else:
        messagebox.showinfo("Login failed", "Incorrect password or phone number try again")


def get_product_price(cur, product_id):
    query = "SELECT price FROM Product WHERE product_id = %s"
    cur.execute(query, (product_id,))
    result = cur.fetchone()

    if result:
        return result[0]
    else:
        return None


def get_product_stock(cur, product_id):
    query = "SELECT stock FROM Product WHERE product_id = %s"
    cur.execute(query, (product_id,))
    result = cur.fetchone()

    if result:
        return result[0]
    else:
        return None


def add_to_order_item(cur, conn, product_id, quantity, customer_id):
    # Get the current order_id
    order_id = get_latest_order_id(cur, conn, customer_id)

    # Calculate the total price for the selected quantity of the product
    product_price = get_product_price(cur, product_id)
    total_price = product_price * quantity

    # Get the current stock of the product
    current_stock = get_product_stock(cur, product_id)

    if current_stock >= quantity:
        # Update the stock of the product
        new_stock = current_stock - quantity
        update_stock_query = "UPDATE Product SET stock = %s WHERE product_id = %s"
        cur.execute(update_stock_query, (new_stock, product_id))
        conn.commit()

        # Insert the selected product and quantity into the Order_Item table
        insert_order_item_query = """INSERT INTO Order_Item (quantity, price, Order_order_id, Product_product_id)
                                     VALUES (%s, %s, %s, %s)"""
        cur.execute(insert_order_item_query, (quantity, total_price, order_id, product_id))
        conn.commit()

        # Update the total_price in the Order table
        update_order_total_query = """UPDATE my_order SET total_price = total_price + %s WHERE order_id = %s"""
        cur.execute(update_order_total_query, (total_price, order_id))
        conn.commit()

        print(f"Added {quantity} of product {product_id} to cart.")
    else:
        messagebox.showinfo("stock", "Out of stock")


def register(cur, conn, data):
    # encrypt the password
    cust_salt, hashed_password = hash_password(data['password'])
    query = """INSERT INTO customer (
        customer_id,
        first_name,
        last_name,
        email,
        cust_password,
        phone_number,
        gender,
        street,
        building_num,
        city,
        security_salt
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    values = (
        data['customer_id'],
        data['first_name'],
        data['last_name'],
        data['email'],
        hashed_password,
        data['phone_number'],
        data['gender'],
        data['street'],
        data['building_num'],
        data['city'],
        cust_salt
    )

    try:
        cur.execute(query, values)
        conn.commit()
        print("Registration successful!")
    except Exception as e:
        conn.rollback()
        print(f"Error during registration: {e}")


def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(32)  # Generate a random salt
    print(password)
    # Combine the password and salt, and then hash them
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    print(hashed_password)
    # Return the salt and hashed password
    return salt, hashed_password


def verify_password(stored_password, input_password, salt):

    # Hash the input password with the stored salt
    hashed_input_password = hashlib.pbkdf2_hmac('sha256', input_password.encode('utf-8'), salt, 100000)

    print(hashed_input_password)
    print(stored_password)

    # Compare the stored hashed password with the newly hashed input password
    if hashed_input_password == stored_password:
        return True
    else:
        return False


def get_all_products(cursor, conn, search_category_id):
    query = "SELECT * FROM product WHERE category_id = %s"
    cursor.execute(query, (search_category_id,))
    products = cursor.fetchall()

    # No need to close the cursor and connection here

    return products


def get_product(cur, conn, product_id):
    query = """ SELECT description
                FROM product 
                WHERE product_id  = %s"""
    cur.execute(query, (product_id,))
    result = cur.fetchall()
    return result


def get_latest_order_id(cur, conn, customer_id):
    query = """SELECT MAX(order_id)
               FROM my_order
               WHERE Customer_customer_id = %s"""
    cur.execute(query, (customer_id,))
    result = cur.fetchone()

    if result:
        return result[0]
    else:
        return None


def get_order_items(cur, conn, customer_id):
    order_id = get_latest_order_id(cur, conn, customer_id)
    query = """SELECT order_item_id, Product_product_id ,price, quantity 
                FROM order_item 
                WHERE Order_order_id  = %s"""
    cur.execute(query, (order_id,))
    result = cur.fetchall()
    if result:
        return result
    else:
        return None


def update_stock(cur, conn, prod_id, quantity):
    current_stock = get_product_stock(cur, prod_id)
    updated_stock = current_stock + quantity
    update_query = "UPDATE product " \
                   "SET stock = %s " \
                   "WHERE product_id = %s"
    cur.execute(update_query, (updated_stock, prod_id))
    conn.commit()  # Commit the changes to the database


def remove_order_item(cur, conn, order_item_id, price, customer_id):
    # Get the current order_id
    order_id = get_latest_order_id(cur, conn, customer_id)
    query = """SELECT total_price
                FROM my_order 
                WHERE order_id  = %s"""
    cur.execute(query, (order_id,))
    current_price = cur.fetchall()

    # Update the total_price in the Order table
    update_order_total_query = """UPDATE my_order SET total_price = total_price - %s WHERE order_id = %s"""
    cur.execute(update_order_total_query, (price, order_id))
    conn.commit()

    delete_query = "DELETE FROM order_item " \
                   "WHERE order_item_id = %s"

    cur.execute(delete_query, (order_item_id,))
    conn.commit()  # Commit the changes to the database
    print(cur.rowcount, "record(s) deleted")


def get_shipment(cur, conn, customer_id):
    query = """SELECT city, street ,building_num, email 
                    FROM customer 
                    WHERE customer_id  = %s"""
    cur.execute(query, (customer_id,))
    result = cur.fetchall()
    if result:
        return result[0]
    else:
        return None


def get_total_price(cur, conn, customer_id):
    order_id = get_latest_order_id(cur, conn, customer_id)
    total_price_query = """SELECT total_price 
                        FROM my_order 
                        WHERE order_id  = %s"""
    cur.execute(total_price_query, (order_id,))
    total = cur.fetchone()
    if total:
        return total[0]
    else:
        return None


def create_shipment(cur, conn, customer_id):
    order_id = get_latest_order_id(cur, conn, customer_id)
    amount = get_total_price(cur, conn, customer_id)
    payment_id = create_payment(cur, conn, order_id, amount)

    shipment_city, shipment_street, shipment_building_num, email = get_shipment(cur, conn, customer_id)

    insert_shipment_query = """INSERT INTO shipment (Order_order_id, shipment_date, shipment_city,
     shipment_street, shipment_building_num, email)
               VALUES (%s, NOW(), %s, %s, %s, %s)"""
    values = (order_id, shipment_city, shipment_street, shipment_building_num, email)
    cur.execute(insert_shipment_query, values)
    conn.commit()

    query = """SELECT shipment_id
                FROM shipment 
                WHERE Order_order_id  = %s"""
    cur.execute(query, (order_id,))
    shipment_id_result = cur.fetchone()  # Use fetchone() to retrieve a single result row
    shipment_id = shipment_id_result[0]  # Extract the shipment_id value

    update_my_order_query = """UPDATE my_order SET shipment_id = %s
     , payment_id=%s WHERE order_id = %s"""

    values = (shipment_id, payment_id, order_id)
    cur.execute(update_my_order_query, values)
    conn.commit()


def create_payment(cur, conn, order_id, amount):
    query = "INSERT INTO payment (payment_date,payment_method,amount,Order_order_id) " \
            "VALUES (NOW(),'Credit Card', %s,%s)"
    values = (amount, order_id)
    cur.execute(query, values)
    conn.commit()

    query = """SELECT payment_id
                FROM payment 
                WHERE Order_order_id  = %s"""
    cur.execute(query, (order_id,))
    payment_id_result = cur.fetchone()  # Use fetchone() to retrieve a single result row
    payment_id = payment_id_result[0]  # Extract the payment_id value
    return payment_id


def create_new_order(cur, conn, customer_id):
    create_order_query = """INSERT INTO my_order (order_date, total_price,
     Customer_customer_id, shipment_id, payment_id)
                            VALUES (NOW(), 0.0, %s, NULL, NULL)"""
    cur.execute(create_order_query, (customer_id,))
    conn.commit()


def delete_order(cur, conn, customer_id):
    order_id = get_latest_order_id(cur, conn, customer_id)

    query = """SELECT quantity, Product_product_id
                    FROM order_item 
                    WHERE Order_order_id  = %s"""
    cur.execute(query, (order_id,))
    result = cur.fetchall()

    for i, (quantity, product_id) in enumerate(result, start=0):
        update_stock(cur, conn, product_id, quantity)

    delete_order_items_query = "DELETE FROM order_item " \
                               "WHERE Order_order_id = %s"
    cur.execute(delete_order_items_query, (order_id,))
    conn.commit()  # Commit the changes to the database

    delete_my_order_query = "DELETE FROM my_order " \
                            "WHERE order_id = %s"
    cur.execute(delete_my_order_query, (order_id,))
    conn.commit()  # Commit the changes to the database


def set_shipment(cur, conn, new_city, new_street, bui_num, customer_id):
    cust_city, cust_street, cust_bui_num, cust_email = get_shipment(cur, conn, customer_id)
    if new_city != cust_city:
        update_city_query = """UPDATE customer SET city =%s  WHERE customer_id = %s"""
        cur.execute(update_city_query, (new_city, customer_id))
        conn.commit()
    if new_street != cust_street:
        update_street_query = """UPDATE customer SET street =%s   WHERE customer_id = %s"""
        cur.execute(update_street_query, (new_street, customer_id))
        conn.commit()
    if bui_num != cust_bui_num:
        update_bui_num_query = """UPDATE customer SET building_num =%s   WHERE customer_id = %s"""
        cur.execute(update_bui_num_query, (bui_num, customer_id))
        conn.commit()


def get_all_cust_order_id(cur, conn, customer_id):
    order_ids_query = """SELECT order_id
               FROM my_order
               WHERE Customer_customer_id = %s"""
    cur.execute(order_ids_query, (customer_id,))
    result = cur.fetchall()
    return result


def get_cust_order(cur, order_id):
    query = f"""
        SELECT 
            shipment.shipment_date, shipment.shipment_city,
            shipment.shipment_street, shipment.shipment_building_num,
            payment.amount,
            shipment.email
        FROM shipment
            NATURAL JOIN payment
        WHERE payment.Order_order_id = %s;"""

    cur.execute(query, order_id)
    result = cur.fetchall()
    return result


def get_order_product(cur, order_id):
    query = """SELECT Product_product_id,quantity
                    FROM order_item 
                    WHERE Order_order_id  = %s"""
    cur.execute(query, (order_id,))

    product_info = cur.fetchall()
    print(product_info)
    cust_product_info = []
    for row, (product_id, qty) in enumerate(product_info, start=1):
        query = """SELECT description, price
                     FROM product
                     WHERE product_id = %s"""
        cur.execute(query, (product_id,))
        product_data = cur.fetchone()
        if product_data:
            cust_product_info.append((product_data[0], product_data[1], qty))
    # return product_info
    print(cust_product_info)
    return cust_product_info
