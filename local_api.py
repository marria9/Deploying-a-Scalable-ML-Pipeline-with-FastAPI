import json

import requests

# TODO: send a GET using the URL http://127.0.0.1:8000
r = "http://127.0.0.1:8000/"
get_response = requests.get(r)
# Your code here

# TODO: print the status code
# print()
print("Status Code:", get_response.status_code)
# TODO: print the welcome message
# print()
print("Welcome message:", get_response.json())


data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# TODO: send a POST using the data above
r = "http://127.0.0.1:8000/data/"
post_response = requests.post(r, json = data)
# Your code here

# TODO: print the status code
# print()
print("Status Code:", post_response.status_code)
# TODO: print the result
# print()
print("Result", post_response.json())
