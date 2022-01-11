# CMPUT 404 Lab 1
import requests

# Part 1: Print out the version of the requests library
print("Requests Version: " + requests.__version__)

# Part 2: Modify python script to make a GET Response to Google's homepage
URL = "http://google.com"
r = requests.get(url = "http://google.com")
print("Google Response:",r)

# Part 3: Modify Python script so that it downloads itself from GitHub and prints out its own source code from GitHub.
rawURL = "https://raw.githubusercontent.com/Proxieds/CMPUT404Lab1/main/requestVersion.py"
request = requests.get(url = rawURL)
print("Raw Url Response:",request)
print(request.content)
