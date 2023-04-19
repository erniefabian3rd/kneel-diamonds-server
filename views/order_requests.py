import sqlite3
import json
from models import Order, Size, Style, Metal

ORDERS = [
    {
        "id": 1,
        "metalId": 3,
        "sizeId": 2,
        "styleId": 3
    }
]

def get_all_orders():
    """Gets all orders"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                o.id,
                o.timestamp,
                o.size_id,
                o.style_id,
                o.metal_id,
                m.metal metal_name,
                m.price metal_price,
                s.carets size_carets,
                s.price size_price,
                st.style style_name,
                st.price style_price
            FROM `Order` o
            JOIN Metal m ON m.id = o.metal_id
            JOIN Size s ON s.id = o.size_id
            JOIN Style st ON st.id = o.style_id
            """)

        orders = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            order = Order(row['id'], row['timestamp'], row['metal_id'], row['size_id'], row['style_id'])

            metal = Metal(row['id'], row['metal_name'], row['metal_price'])

            size = Size(row['id'], row['size_carets'], row['size_price'])

            style = Style(row['id'], row['style_name'], row['style_price'])

            order.metal = metal.__dict__
            order.size = size.__dict__
            order.style = style.__dict__

            orders.append(order.__dict__)

    return orders

def get_single_order(id):
    """Gets single order by id"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id,
            o.timestamp,
            o.metal_id,
            o.size_id,
            o.style_id
        FROM 'Order' o
        WHERE o.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        order = Order(data['id'], data['timestamp'], data['metal_id'], data['size_id'],
                            data['style_id'])
        
        return order.__dict__


def create_order(new_order):
    """Places a new order"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            INSERT INTO 'Order'
                ( timestamp, metal_id, size_id, style_id )
            VALUES
                ( ?, ?, ?, ?);
            """, (new_order['timestamp'], new_order['metal_id'],
                new_order['size_id'], new_order['style_id'] ))

        id = db_cursor.lastrowid
        new_order['id'] = id

    return new_order

def delete_order(id):
    """Deletes a single order by id"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM 'Order'
        WHERE id = ?
        """, (id, ))

def update_order(id, new_order):
    """Updates order with client's replacement"""

    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break
