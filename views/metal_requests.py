import sqlite3
import json

METALS = [
    {
        "id": 1,
        "metal": "Sterling Silver",
        "price": 12.42
    },
    {
        "id": 2,
        "metal": "14K Gold",
        "price": 726.4
    },
    {
        "id": 3,
        "metal": "24K Gold",
        "price": 1258.9
    },
    {
        "id": 4,
        "metal": "Platinum",
        "price": 795.45
    },
    {
        "id": 5,
        "metal": "Palladium",
        "price": 1241.0
    }
]

def get_all_metals():
    """Gets all metals"""
    return METALS

def get_single_metal(id):
    """Gets single metal"""
    requested_metal = None

    for metal in METALS:
        if metal["id"] == id:
            requested_metal = metal

    return requested_metal

def update_metal(id, new_metal):
    """Updates metal with client information"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Metal
            SET
                metal = ?,
                price = ?
        WHERE id = ?
        """, (new_metal['metal'], new_metal['price'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True