# clutch-geolocator
a web service that can do some basic geolocation


## Prerequisites
You must have docker installed

## Set up
Clone the repository and run setup.sh with the API key that was emailed to you
~~~
git clone https://github.com/luke-grantham/clutch-geolocator.git
cd clutch-geolocator
./setup.sh paste-api-key-here
~~~

## Use
Given an address, return the US state that contains that address

Send an HTTP GET request to `localhost:5000/address` and include a header named address whose value is the address you want to lookup

Example with curl:

`curl http://127.0.0.1:5000/address --header "address: 3535 Piedmont Ave, Suite 1500, Atlanta, GA 30305"`

### troubleshooting

If you have changed the default subnet for your Docker installation, you'll need to run `docker network inspect bridge`, find your Gateway IP, change the variable `docker_gateway_ip` inside `server.py` to that value, then run the setup script again.
