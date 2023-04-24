import sqlite3
import json
from models import Style

STYLES = [
    {
        "id": 1,
        "style": "Classic",
        "price": 500
    },
    {
        "id": 2,
        "style": "Modern",
        "price": 710
    },{
        "id": 3,
        "style": "Vintage",
        "price": 965
    }
]

def get_all_styles(query_params):
    """Gets all styles"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        sort_by = ""

        if len(query_params) != 0:
            param = query_params[0]
            [qs_key, qs_value] = param.split("=")

            if qs_key == "_sortBy":
                if qs_value == 'price':
                    sort_by = "ORDER BY st.price DESC"

        sql_to_execute = f"""
            SELECT
                st.id,
                st.style,
                st.price
            FROM Style st
            {sort_by}
            """

        db_cursor.execute(sql_to_execute)

        styles = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            style = Style(row['id'], row['style'], row['price'])

            styles.append(style.__dict__)

    return styles

def get_single_style(id):
    """Gets single style"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            st.id,
            st.style,
            st.price
        FROM Style st
        WHERE st.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()
        style = Style(data['id'], data['style'], data['price'])

        return style.__dict__
