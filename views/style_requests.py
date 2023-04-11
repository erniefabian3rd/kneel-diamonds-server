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

def get_all_styles():
    """Gets all styles"""
    return STYLES

def get_single_style(id):
    """Gets single style"""
    requested_style = None

    for style in STYLES:
        if style["id"] == id:
            requested_style = style

    return requested_style
