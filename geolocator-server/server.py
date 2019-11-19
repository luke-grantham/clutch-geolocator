import requests
import sys
import urllib.parse

from http.server import BaseHTTPRequestHandler, HTTPServer

class GeocodeHandler(BaseHTTPRequestHandler):
        
        def do_GET(self):
                address = urllib.parse.quote_plus("1600 Amphitheatre Parkway, Mountain View, California")
                key = "redacted"

                url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + address + "&key=" + key

                self.send_header('Content-type','text/html')
                self.end_headers()

                response = requests.get(url)

                lat = response.json()['results'][0]['geometry']['location']['lat']
                lng = response.json()['results'][0]['geometry']['location']['lng']
                faddress = response.json()['results'][0]['formatted_address']
                
                message = str(lat) + "," + str(lng)
                self.wfile.write(bytes(message, "utf8"))
                
                self.send_response(200)
                return

        
def run(server_class=HTTPServer, handler_class=GeocodeHandler):
    server_address = ('', 9900)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()

