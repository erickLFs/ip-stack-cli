# CLI IP Geolocation
This Python repository is designed to perform IP geolocation, a process that determines the geographical coordinates (latitude and longitude) associated with a given IP address. It's a command-line tool that allows you to input an IP address as an argument, and it will retrieve and display the corresponding latitude and longitude information for that IP.

## Set up the project
Before using the application,  you must create an account and have a valid token to run the application, which you can obtain at this [URL](https://ipstack.com/signup/free)

> You need to add your token to the .env file **API_TOKEN=your_token**

# Run the application
To run the application, you must have Python installed.

Intsall the requirements:
```
pip install -r requirements.txt
```
Executhe the command: 
```
python main 12.1.1.1
```
# Run the application with Docker

To run the application, you must have Docker installed.

## Generate the docker container
```
docker build -t ip-cli .
```

## Run the docker container 
```
docker run -it ip-cli
```
execute the program: 
```
python main.py 12.1.1.1
```
### Example response
```
{
    "latitude": 40.7589111328125,
    "longitude": -73.97901916503906,
    "message": "OK",
    "status": 200
}
```