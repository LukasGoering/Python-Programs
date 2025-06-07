''' This web app implements a financial transaction recording system using Flask.
The system implements the CRUD actions:
It is capable of Creating a new entry, Reading existing entries,
Updating existing entries, and Deleting existing entries.

It has three different web pages:
- Transaction Records: Displays all recorded transactions with options to Edit and Delete entries, and to add a new entry.
- Add Transaction: Used to add a new transaction entry by providing Date and Amount.
- Edit Transaction: Allows editing of an existing transaction entry by updating the Date and Amount for a specific ID.

Run the server by executing this file by Python
'''

# Import libraries
from flask import Flask, request, url_for, redirect, render_template

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Sample data (optional)
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]


# Read operation: List all transactions
@app.route('/')
def get_transactions():
    """Return a list of transactions."""
    return render_template('transactions.html', transactions=transactions)
    # transactions.html is the name of the HTML template file in the templates folder.
    # transactions=transactions passes the dictionary defined above to the template.


# Create operation: Display add transaction form and handle form submission
@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    ''' Allows to add a transaction
        GET: Shows webpage with a form to enter the new transaction
        POST: Adds the new transaction assigning a new id.
    '''
    if request.method == 'GET':
        return render_template('form.html')
    
    elif request.method == 'POST':
        transaction = {
                # Default ID is the current number of transactions + 1
                'id': len(transactions) + 1,
                'date': request.form['date'],
                'amount': float(request.form['amount'])
                }
        transactions.append(transaction)
        return redirect(url_for('get_transactions'))


# Update operation
@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    ''' Allows to edit the transaction with the given id
        GET: Shows webpage with a form to edit the transaction
        POST: Updates the transaction with the given id
    '''
    # Check if there exists a transaction with the given id.
    if not any(transaction['id'] == transaction_id for transaction in transactions):
        return {"message": "Transaction not found"}, 404

    if request.method == 'GET':
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                return render_template('edit.html', transaction=transaction)
    
    if request.method == 'POST':
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = request.form['date']
                transaction['amount'] = float(request.form['amount'])
                return redirect(url_for('get_transactions'))


# Delete operation
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    ''' Allows to delete a transaction '''
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            return redirect(url_for('get_transactions')) # Refreshes the transaction list


@app.route('/search', methods=['GET', 'POST'])
def search_transactions():
    ''' This function allows filtering the transaction list by the amount.
        GET: Opens webpage with a form to enter the minimum and maximum amount.
        POST: Displays the filtered transaction list.
        Input format: Both minimum and maximum amounts should be numeric values.
    '''
    if request.method == 'GET':
        return render_template('search.html')

    if request.method == 'POST':
        # Retrieve the minimum and maximum amount from the user form
        try:
            min_filter = float(request.form['min_amount'])
            max_filter = float(request.form['max_amount'])
        except ValueError:
            return {"message": "Invalid input. Please enter numeric values for the amount filters."}, 400

        # Create the filtered transaction list.
        # This could be made more efficient using list comprehension
        filtered_transactions = [] # Initialize as a list
        for transaction in transactions:
            if transaction['amount'] >= min_filter and transaction['amount'] <= max_filter:
                filtered_transactions.append(transaction)
        return render_template('transactions.html', transactions=filtered_transactions)


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
