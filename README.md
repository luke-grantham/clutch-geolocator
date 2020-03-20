# take-home-interview-geolocator
This is a take-home interview I finished. It is a python REST API with a single endpoint that will return the US state that contains the given address. The assignment required an API call to Google's Maps API and a lookup from a geography data set loaded in PostgreSQL.


## Prerequisites
You must have docker installed

## Set up
Clone the repository and run setup.sh with the API key that was emailed to you
~~~
git clone https://github.com/luke-grantham/take-home-interview-geolocator.git
cd take-home-interview-geolocator
./setup.sh paste-api-key-here
~~~

You can run `docker ps` to check that two docker containers have been started.

## Use
Given an address, return the US state that contains that address

Send an HTTP GET request to `localhost:5000/address` and include a header named `address` whose value is the address you want to lookup

Example with curl:

`curl http://127.0.0.1:5000/address --header "address: 1600 Amphitheatre Parkway"`

### troubleshooting

If you have changed the default subnet for your Docker installation, you'll need to run `docker network inspect bridge`, find your Gateway IP, change the variable `docker_gateway_ip` inside `server.py` to that value, then run the setup script again.
