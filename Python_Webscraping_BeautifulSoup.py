from bs4 import BeautifulSoup
import requests

# Save HTML as a string
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html5lib')
# Print the prettified HTML
#print(soup.prettify())

## Tags
# The Tag object corresponds to an HTML tag in the original document, for example, the tag title.
# If there is more than one Tag with the same name, the first element with that Tag name is called.
tag_object=soup.title
print("tag object:",tag_object)
print("tag object type:",type(tag_object))  # Tag type

# First Element with the Tag name is the most paid player
tag_object = soup.h3    # First h3 tag (use find_all() to get all h3 tags)
print(tag_object)
# Navigate to the child tag
tag_child = tag_object.b
print(tag_child)
# Navigate back to the parent tag
parent_tag = tag_child.parent
print(parent_tag)           # Identical to the h3 tag tag_object
# The next paragraph is the next sibling of the h3 tag
sibling_1 = tag_object.next_sibling
print(sibling_1)
# Access atrributes of the tag (treat it like a dictionary)
print(tag_child['id'])
print(tag_child.get('id'))
print(tag_child.attrs)

## Navigable string
# A string corresponds to a bit of text or content within a tag. Beautiful Soup uses the NavigableString class to contain this text.
tag_string = tag_child.string
print(tag_string)
print(type(tag_string))  # NavigableString type
# A NavigableString is a subclass of Unicode string, so you can use it like a normal string but it supports some Beautiful Soup methods.
unicode_string = str(tag_string)
print(unicode_string)

## Filter
# Store an HTML table in a string
table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, 'html5lib')

# Extract all rows from the table
table_rows = table_bs.find_all('tr')
first_row = table_rows[0]
first_cell_first_row = first_row.td # Obtain as the child of first_row

# Print all rows of the table
for i, row in enumerate(table_rows):
    print("row", i, "is", row)
    # Print all cells of the corresponding row
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)

# Filter the table by id
print(table_bs.find_all(id="flight"))

# Filter the table by href
print(table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida"))

# Find all tags with an href value
print(table_bs.find_all(href=True))

# Search for strings instead of tags:
print(table_bs.find_all(string="Florida"))