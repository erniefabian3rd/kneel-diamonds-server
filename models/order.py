class Order():
    """Class to contain all order fields"""

    def __init__(self, id, timestamp, metal_id, size_id, style_id):
        self.id = id
        self.timestamp = timestamp
        self.metal_id = metal_id
        self.size_id = size_id
        self.style_id = style_id
        self.metal = None
        self.size = None
        self.style = None