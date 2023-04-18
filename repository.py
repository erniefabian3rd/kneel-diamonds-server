DATABASE = {
    "metals": [
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
    ],
    "sizes": [
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
    ],
    "styles": [
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
    ],
    "orders": [
        {
            "id": 1,
            "timestamp": 1614659931693,
            "metal_id": 3,
            "size_id": 2,
            "style_id": 3
        }
    ]
}

def all(resource):
    """For GET requests to collection"""
    return DATABASE[resource]



def retrieve(resource, id, query_params):
    """For GET requests to a single resource"""
    requested_resource = None
    for item in DATABASE[resource]:
        if item["id"] == id:
            requested_resource = item

    if resource == "orders":
        requested_order = requested_resource.copy()
        
        matching_metal = retrieve("metals", requested_order["metal_id"], query_params)
        if "expand=metal" in query_params:
            requested_order["metal"] = matching_metal
            requested_order.pop("metal_id")

        matching_size = retrieve("sizes", requested_order["size_id"], query_params)
        if "expand=size" in query_params:
            requested_order["size"] = matching_size
            requested_order.pop("size_id")

        matching_style = retrieve("styles", requested_order["style_id"], query_params)
        if "expand=style" in query_params:
            requested_order["style"] = matching_style
            requested_order.pop("style_id")

        requested_order["price"] = matching_metal["price"] + matching_size["price"] + matching_style["price"]

        return requested_order

    return requested_resource


def create(resource, post_body):
    """For POST requests to a collection"""
    max_id = DATABASE[resource][-1]["id"]
    new_id = max_id + 1
    post_body["id"] = new_id
    DATABASE[resource].append(post_body)

    return post_body

def update(resource, id, post_body):
    """For PUT requests to a single resource"""
    for index, item in enumerate(DATABASE[resource]):
        if item["id"] == id:
            DATABASE[resource][index] = post_body
            break

# Delete function not needed for purpose of this project
# In real world, code would not exist here.

# def delete(resource, id):
#     """For DELETE requests to a single resource"""
#     resource_index = -1
#     for index, item in enumerate(DATABASE[resource]):
#         if item["id"] == id:
#             resource_index = index

#     if resource_index >= 0:
#         DATABASE[resource].pop(resource_index)
