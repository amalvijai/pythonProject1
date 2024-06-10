from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/orderDetails')
def order_details():
    return render_template('order_details.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if username and password match
        if username == 'admin' and password == 'admin':
            # Redirect to new page route
            return redirect(url_for("order_details"))
        else:
            # If credentials are incorrect, render login page again with an error message
            return render_template('login.html', error=True)
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration logic here
        username = request.form['username']
        password = request.form['password']
        # Save user information (e.g., save to database)
        return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
