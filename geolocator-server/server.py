#!flask/bin/python
from flask import Flask
from flask import request
import sys
import urllib.parse
import requests
import psycopg2

app = Flask(__name__)
key = sys.argv[1]
docker_gateway_ip="172.17.0.1"

def geocode(addr):
    """take a string address and return a lat,long tuple"""

    address = urllib.parse.quote_plus(addr)
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + address + "&key=" + key
 
    response = requests.get(url)

    if response.json()['status'] == 'OK':
        return (response.json()['results'][0]['geometry']['location']['lat'], response.json()['results'][0]['geometry']['location']['lng'])
    elif response.json()['status'] == 'ZERO_RESULTS':
        return (1000,"Zero Results from Google API")
    else:
        return (1001,"Unknown Error from Google Maps API")

def get_state_from_coords(lat_lng):
    """take a 2-tuple of floats representing latitude and longitude. return the containing US state or an error message"""

    # Check for errors from Google Maps API
    if lat_lng[0] == 1000:
        return lat_lng[1]
    elif lat_lng[0] == 1001:
        return lat_lng[1]

    conn = psycopg2.connect(host=docker_gateway_ip, port = 5432, database="postgres", user="postgres")
    cur = conn.cursor()

    cur.execute("SELECT NULLIF(name, '') FROM gis.states where ST_CONTAINS(geom, ST_SetSRID( ST_POINT(" + str(lat_lng[1]) + "," + str(lat_lng[0]) + "), 4326))")

    query_results = cur.fetchall()

    cur.close()
    conn.close()
   
    if len(query_results) > 0:
        return query_results[0][0]
    else:
        return "That address is outside the United States"

@app.route('/address',methods = ['GET'])
def index():
    try:
        return get_state_from_coords(geocode(request.headers['address']))
    except KeyError as e:
        return "Your request must include a header named 'address'"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
