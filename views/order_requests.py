from .metal_requests import get_single_metal
from .size_requests import get_single_size
from .style_requests import get_single_style

ORDERS = [
    {
        "id": 1,
        "timestamp": 1614659931693,
        "metalId": 3,
        "sizeId": 2,
        "styleId": 3
    }
]

def get_all_orders():
    """Gets all orders"""
    return ORDERS

def get_single_order(id):
    """Gets single order"""
    requested_order = None

    for order in ORDERS:
        if order["id"] == id:
            requested_order = order

            matching_metal = get_single_metal(requested_order["metalId"])
            requested_order["metal"] = matching_metal
            requested_order.pop("metalId")

            matching_size = get_single_size(requested_order["sizeId"])
            requested_order["size"] = matching_size
            requested_order.pop("sizeId")

            matching_style = get_single_style(requested_order["styleId"])
            requested_order["style"] = matching_style
            requested_order.pop("styleId")

    return requested_order

def create_order(order):
    """Places a new order"""
    max_id = ORDERS[-1]["id"]
    new_id = max_id + 1
    order["id"] = new_id

    ORDERS.append(order)

    return order

def delete_order(id):
    """Deletes order"""
    order_index = -1

    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            order_index = index

    if order_index >= 0:
        ORDERS.pop(order_index)

def update_order(id, new_order):
    """Updates order with client's replacement"""

    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break
