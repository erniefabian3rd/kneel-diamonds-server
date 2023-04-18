import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_metals, get_single_metal
from views import get_all_orders, get_single_order, create_order
from views import get_all_sizes, get_single_size
from views import get_all_styles, get_single_style


class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def do_GET(self):
        """Handles GET requests to the server """

        response = {}

        (resource, id) = self.parse_url(self.path)

        if resource == "metals":
            if id is not None:
                response = get_single_metal(id)
                if response is not None:
                    self._set_headers(200)
                else:
                    self._set_headers(404)
                    response = { "message": "That metal is not currently in stock for jewelry."}
            else:
                self._set_headers(200)
                response = get_all_metals()

        elif resource == "sizes":
            if id is not None:
                response = get_single_size(id)
                if response is not None:
                    self._set_headers(200)
                else:
                    self._set_headers(404)
                    response = {"message": "That size is not currently in stock for jewelry."}
            else:
                self._set_headers(200)
                response = get_all_sizes()

        elif resource == "styles":
            if id is not None:
                response = get_single_style(id)
                if response is not None:
                    self._set_headers(200)
                else:
                    self._set_headers(404)
                    response = {"message": "That style is not currently in stock for jewelry."}
            else:
                self._set_headers(200)
                response = get_all_styles()

        elif resource == "orders":
            if id is not None:
                response = get_single_order(id)
                if response is not None:
                    self._set_headers(200)
                else:
                    self._set_headers(404)
                    response = {"message": "That order was never placed, or was cancelled."}
            else:
                self._set_headers(200)
                response = get_all_orders()

        else:
            response = []

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Handles POST requests to the server """

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        new_order = None

        if resource == "orders":
            if "timestamp" in post_body and "metal_id" in post_body and "size_id" in post_body and "style_id" in post_body:
                self._set_headers(201)
                new_order = create_order(post_body)
            else:
                self._set_headers(400)
                new_order = {
                    "message": f'{"timestamp is required" if "timestamp" not in post_body else ""}{"metal Id is required" if "metal_id" not in post_body else ""}{"size Id is required" if "size_id" not in post_body else ""}{"style Id is required" if "style_id" not in post_body else ""}'
                }
            self.wfile.write(json.dumps(new_order).encode())

    def do_PUT(self):
        """Handles PUT requests to the server """
        update_order_message = None
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        if resource == "orders":
            self._set_headers(405)
            update_order_message = {
                "message": f'{"Order has already been processed and is in production. Unable to update order at this time. Please contact customer support."}'
            }
            self.wfile.write(json.dumps(update_order_message).encode())


    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_DELETE(self):
        """Handles DELETE requests to the server"""
        delete_order_message = None

        (resource, id) = self.parse_url(self.path)

        if resource == "orders":
            self._set_headers(405)
            delete_order_message = {
                "message": f'{"Order has already been processed and is in production. Unable to delete order at this time. Please contact customer support."}'
            }
            self.wfile.write(json.dumps(delete_order_message).encode())

    def parse_url(self, path):
        """Parses Url"""
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        try:
            id = int(path_params[2])
        except IndexError:
            pass
        except ValueError:
            pass

        return (resource, id)

# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
