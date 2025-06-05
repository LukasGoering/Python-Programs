import requests # Allows to send HTTP/1.1 requests
import os
from PIL import Image
from IPython.display import IFrame

url='https://www.ibm.com/'
r=requests.get(url)
#print("get data:", r)
#print("request status code:", r.status_code)
#print("request headers:", r.request.headers)
#print("request body:", r.request.body)
#print("request first 100 characters of text:", r.text[0:100])

# Obtain a file/image from the web
# An file/image is a response object that is contained in a bytes-like object
# We must save it using a file object
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path=os.path.join(os.getcwd(),'example1.txt')   # Get the current working directory
r=requests.get(url)         # Sends HTTP GET request to the URL
with open(path,'wb') as f:  #"wb" means write in binary mode
    f.write(r.content)      # Write the content of the response to the file

# Get request with URL parameters
url_get='http://httpbin.org/get'        # URL to send the GET request
payload={"name":"Joseph","ID":"123"}    # Query string parameters
r=requests.get(url_get, params=payload) # Send the GET request with parameters
print("Resulting URL:", r.url)
print("Status Code:", r.status_code)
print("Response as text:", r.text)
print("Content is in the JSON format:", r.json()) # Convert the response to JSON

# Post request with URL parameters
url_post='http://httpbin.org/post'
payload={"name":"Joseph","ID":"123"}    # Same as before
r_post=requests.post(url_post,data=payload)

