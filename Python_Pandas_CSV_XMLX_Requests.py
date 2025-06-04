import pandas as pd
import numpy as np
import requests
import urllib.request

def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:      # Check if the request was successful
        with open(filename, "wb") as file:
            file.write(response.content)

def main():
    ### CSV file example
    csv_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"
    download(csv_url, "addresses.csv")
    df = pd.read_csv("addresses.csv", header=None)

    # Add column names
    df.columns = ['First Name', 'Last Name', 'Location ', 'City', 'State', 'Area Code']
    # Select multiple columns
    selected_columns = df[["First Name", "Last Name"]]
    # Select rows using .iloc and .loc
    # Select the first row
    first_row = df.loc[0]
    # Select the first three rows of column "First Name" only
    var1 = df.loc[[0, 1, 2], "First Name"]
    var2 = df.iloc[[0,1,2], 0] # Indexed based selecting method

    print("Selected columns:\n", selected_columns)
    print("First row:\n", first_row)
    print("First three First Names (.loc/.iloc):")
    print(var1)
    print(var2)


    # XLSX file example
    urllib.request.urlretrieve("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx", "sample.xlsx")
    ibm_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx"
    download(ibm_url, "file_example_XLSX_10.xlsx")
    df = pd.read_excel("file_example_XLSX_10.xlsx")
    print(df)


if __name__ == "__main__":
    main()