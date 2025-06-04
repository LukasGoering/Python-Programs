import json

# Create a dictionary
person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

# Save the dictionary to a JSON file
# 1. Parameter: dictionary to be converted to JSON object.
# 2. Parameter: file pointer of the file opened in write or append mode.
with open('Python_JSON_person.json', 'w') as json_file:
    json.dump(person, json_file, indent=4)     # indent=4 makes the JSON file more readable

# Read the JSON file using json.load()
with open('Python_JSON_person.json', 'r') as json_file:
    data = json.load(json_file)     # Type: Python dictionary
    print(data)  # Print the loaded JSON data