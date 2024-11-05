from flask import Flask, request
import sys
from typing import *

from flask_cors import CORS

from rest_inteface import RestInterface


class TusLibrosWebServer:
    def __init__(self):
        self.app = Flask(__name__)
        self.rest_interface = RestInterface()
        CORS(self.app)

        @self.app.route("/createCart")
        def create_cart():
            params = request.args.to_dict()
            response = self.rest_interface.create_cart(int(params["user_id"]), params["password"])
            return response["body"]

    def listening_on(self, port: int):
        self.app.run(port=port)


if __name__ == "__main__":
    port = int(sys.argv[1])
    server = TusLibrosWebServer()
    server.listening_on(port)
