from flask import Flask, render_template, request

app = Flask(__name__)

# In-memory storage for demonstration purposes
users_db = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_credentials():
    username = request.form['username']
    password = request.form['password']

    if username in users_db:
        return "Username already exists", 400

    users_db[username] = password
    return "Credentials submitted successfully"


@app.route('/view_passwords')
def view_passwords():
    return render_template('view_passwords.html', users=users_db)


if __name__ == '__main__':
    app.run(debug=True)
