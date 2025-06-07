''' This is a simple Flask server that responds with "Hello, World!" when accessed at the root URL. '''
# To run this code, you need to have Flask installed.
# Navigate to the directory where this file is located and run the following command:
# python -m flask --app server --debug run
# The server will start. Notice the line "Running on https://127.0.0.1:5000.
# This is the same as localhost:5000.
# Split the terminal and run the following command:
# curl.exe -X GET -i -w '\n' localhost:5000
# Note that curl.exe is needed instead of curl, since curl is not available on Windows by default.

# Import the Flask class from the flask module
from flask import Flask, make_response, request

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)


## Create a simple function that returns a dictionary as a response
# No comments between the route decorator and the function definition!
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Create a dictionary to return as a response
    return {"message": "Hello World"}

# Create a method without content returning a 204 No Content response
@app.route("/no-content")
def no_content():
    """Return 'no content found' with a status of 204.

    Returns:
        tuple: A tuple containing a dictionary and a status code.
    """
    return {"message": "Not content found"}, 204

# Define a route for the "/exp" URL
@app.route("/exp")
def index_explicit():
    """Return 'Hello World' message with a status code of 200.

    Returns:
        response: A response object containing the message and status code 200.
    """
    resp = make_response({"message": "Hello, World"})
    resp.status_code = 200
    return resp

# Import hardcoded data to simulate a database
data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

@app.route("/data")
def get_data():
    '''
        Check if 'data' exists.
        If 'data' is empty, return a 500 Internal Server Error. 
        If 'data' is not defined, return a 404 Not Found error.
        If 'data' exists, return a message indicating the length of the data.
    '''
    try:
        # Check if 'data' exists and has a length greater than 0
        if data and len(data) > 0:
            # Return a JSON response with a message indicating the length of the data
            return {"message": f"Data of length {len(data)} found"}
        else:
            # If 'data' is empty, return a JSON response with a 500 Internal Server Error status code
            return {"message": "Data is empty"}, 500
    except NameError:
        # Handle the case where 'data' is not defined
        # Return a JSON response with a 404 Not Found status code
        return {"message": "Data not found"}, 404
    

@app.route("/name_search")
def name_search():
    """ Find a person in the database.
    Returns:
        json: Person if found, with status of 200
        404: If not found
        400: If argument 'q' is missing
        422: If argument 'q' is present but invalid
    """
    # Get the argument 'q' from the query parameters of the request
    query = request.args.get('q')

    # Check if the query parameter 'q' is missing
    if query is None:
        return {"message": "Query parameter 'q' is missing"}, 400
    
    # Check if the query parameter is present but invalid (e.g., empty or numeric)
    if query.strip() == "" or query.isdigit():
        return {"message": "Invalid input parameter"}, 422
    
    # Iterate through the 'data' list to look for the person whose first name matches the query
    for person in data:
        if query.lower() in person["first_name"].lower():
            return person, 200
        
    # If no person is found, return a 404 Not Found response
    return {"message": "Person not found"}, 404


@app.route("/count")
def count():
    """Count the number of people in the database.
    Returns:
        json: Count of people if found, with status of 200
    """
    try:
        return {"Data count": len(data)}, 200
    except NameError:
        # If 'data' is not defined and raises a NameError
        # Return a JSON response with a 500 Internal Server Error status code
        return {"message": "data not defined"}, 500
    

@app.route("/person/<var_name>")
def find_by_uuid(var_name):
    ''' Find a person by their UUID.
    Args:
        var_name (str): The UUID of the person to find.
    Returns:
        200: Person as JSON if found
        404: If not found
    '''
    for person in data:
        if person["id"] == str(var_name):
            return person, 200
    return {"message": "Person not found"}, 404


@app.delete("/person/<uuid:id>")
def delete_by_uuid(id):
    ''' Delete a person by their UUID.
    Args:
        id (str): The UUID of the person to delete.
    Returns:
        200: Person deleted successfully
        404: If not found
    '''
    for idx, person in enumerate(data):
        if person["id"] == str(id):
            del data[idx]
            return {"message": f"Person with ID {id} deleted"}, 200
    return {"message": "Person not found"}, 404


@app.post("/person")
def add_by_uuid():
    ''' Add a new person from JSON data in the request body to the database.
    Args: None
    Returns:
        200: Person's ID and message if added successfully
        422: If the request body was not found or invalid
    '''
    # Get the JSON data from the request body
    json_data = request.get_json()

    # Check if the JSON data is None or empty
    if json_data is None or not json_data:
        return {"message": "Invalid request body"}, 422
    
    # Check if the required fields are present in the JSON data
    required_fields = ["id", "first_name", "last_name", "graduation_year", "address", "city", "zip", "country", "avatar"]
    for field in required_fields:
        if field not in json_data:
            return {"message": f"Missing required field: {field}"}, 422
        
    # Check if a person with the same ID already exists
    for person in data:
        if person["id"] == json_data["id"]:
            return {"message": f"Person with ID {json_data['id']} already exists"}, 422    
    
    # If all checks pass, try to add the new person to the 'data' list
    try:
        data.append(json_data)
    except NameError:
        return {"message": "Data not defined"}, 500
    
    # Finally, return a success message with the person's ID
    return {"message": f"Person with ID {json_data['id']} added successfully"}, 200


@app.route("/test500")
def test500():
    ''' Test route to force a 500 Internal Server Error
        This is for testing purposes only and should not be used in production.
    '''
    raise Exception("Forced exception for testing")

@app.errorhandler(404)
def api_not_found(error):
    ''' Custom error handler for 404 Not Found. '''
    return {"message": "The requested URL was not found."}, 404

@app.errorhandler(Exception)
def handle_exception(e):
    return {"message": str(e)}, 500
