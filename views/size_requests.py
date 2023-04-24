import sqlite3
import json
from models import Size

SIZES = [
    {
        "id": 1,
        "carets": 0.5,
        "price": 405
    },
    {
        "id": 2,
        "carets": 0.75,
        "price": 782
    },
    {
        "id": 3,
        "carets": 1,
        "price": 1470
    },
    {
        "id": 4,
        "carets": 1.5,
        "price": 1997
    },
    {
        "id": 5,
        "carets": 2,
        "price": 3638
    }
]

def get_all_sizes(query_params):
    """Gets all sizes"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        sort_by = ""

        if len(query_params) != 0:
            param = query_params[0]
            [qs_key, qs_value] = param.split("=")

            if qs_key == "_sortBy":
                if qs_value == 'price':
                    sort_by = "ORDER BY s.price DESC"

        sql_to_execute = f"""
            SELECT
                s.id,
                s.carets,
                s.price
            FROM Size s
            {sort_by}
            """

        db_cursor.execute(sql_to_execute)

        sizes = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            size = Size(row['id'], row['carets'], row['price'])

            sizes.append(size.__dict__)

    return sizes

def get_single_size(id):
    """Gets single size"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            s.id,
            s.carets,
            s.price
        FROM Size s
        WHERE s.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()
        size = Size(data['id'], data['carets'], data['price'])

        return size.__dict__