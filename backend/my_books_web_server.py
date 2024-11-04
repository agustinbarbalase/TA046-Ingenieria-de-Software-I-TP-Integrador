from flask import Flask, request, Response
import sys
from typing import *

from rest_inteface import RestInterface

class TusLibrosWebServer:
    def __init__(self):
        self.app = Flask(__name__)
        self.rest_interface = RestInterface() 
        

        @self.app.route('/createCart')
        def create_cart():
            params = request.args.to_dict()
            BODY = f"Received parameters: {params}"  
            STATUS_STRING = "200 OK" 
            response = self.xxx.create_cart(int(params["user_id"]), params["password"])
            print(response)
            return Response(response=BODY, status=STATUS_STRING)
        


    def listening_on(self, port: int):
        self.app.run(port=port)

if __name__ == '__main__':
    port = int(sys.argv[1])
    server = TusLibrosWebServer()
    server.listening_on(port)

