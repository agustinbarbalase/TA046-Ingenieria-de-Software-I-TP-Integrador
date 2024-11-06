import sys
from flask import Flask, request
from typing import *

from flask_cors import CORS

from rest_interface import RestInterface


class TusLibrosWebServer:
    def __init__(self):
        self.app = Flask(__name__)
        self.rest_interface = RestInterface()
        CORS(self.app)

        @self.app.route("/createCart")
        def create_cart():
            params = request.args.to_dict()
            response = self.rest_interface.create_cart(
                params["userId"], params["password"]
            )
            return response["body"]

        @self.app.route("/listCart")
        def list_cart():
            params = request.args.to_dict()
            response = self.rest_interface.list_cart(params["userId"])
            return response["body"]

        @self.app.route("/addToCart")
        def add_to_cart():
            params = request.args.to_dict()
            response = self.rest_interface.add_to_cart(
                params["userId"], params["bookIsbn"], params["bookQuantity"]
            )
            return response["body"]

    def listening_on(self, port: int):
        self.app.run(port=port)


if __name__ == "__main__":
    port = int(sys.argv[1])
    server = TusLibrosWebServer()
    server.listening_on(port)
