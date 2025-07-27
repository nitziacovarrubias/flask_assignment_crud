from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

@app.route('/')
def get_transactions():
    return render_template('transactions.html', transactions=transactions)

@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        transaction = {
            'id': len(transactions)+1,
            'date': request.form['date'],
            'amount': float(request.form['amount'])
        }
        transactions.append(transaction)
        return redirect(url_for('get_transactions'))

    return render_template('form.html')

@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    if request.method == 'POST':
        date = 'date': request.form['date']
        amount = 'amount': float(request.form['amount'])

        for tran in transactions:
            if tran['id'] == transaction_id:
                tran['date'] = date
                tran['amount'] = amount
                break
                
        return redirect(url_for('get_transactions'))
    
    for tran in transactions:
            if tran['id'] == transaction_id:
                return render_template('edit.html', tran)

    return {'message': 'Transaction not found'}, 404

@app.route('/delete/<int:transaction_id>', method='DELETE')
def delete_transaction(transaction_id):
    for tran in transactions:
        if tran['id'] == transaction_id:
            transactions.remove(tran)
            return redirect(url_for('get_transactions'))
            
    return {'message': 'Transaction not found'}, 404

# Run the Flask app
    