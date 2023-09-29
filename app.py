# Import the Flask module
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and a function to handle the route
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the Flask app
if __name__ == '__main__':
    app.run()