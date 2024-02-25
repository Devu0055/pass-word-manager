# pass-word-manager
PASSWORD MANAGER

Introduction
============

This documentation provides information about the Flask project for managing user credentials.

Overview
--------

The Flask project consists of a web application that allows users to submit their credentials (username and password) and view saved passwords.

Features
--------

- Submit credentials: Users can submit their username and password.
- View saved passwords: Users can view a list of saved passwords.


Installation
============

To run the Flask application locally, follow these steps:

1. Clone the repository:


2. Install dependencies:


3. Run the Flask application:


The application will be running at http://localhost:5000.

Usage
=====

1. Accessing the Application:

   Open a web browser and navigate to http://localhost:5000.

2. Submitting Credentials:

   - On the homepage, fill in the username and password fields in the login form.
   - Click the "Submit" button to submit the credentials.

3. Viewing Saved Passwords:

   - After submitting credentials, you can navigate to the "/view_passwords" endpoint to view the saved passwords.

API Reference
=============

Submit Credentials
------------------

URL: /submit
Method: POST

Description:
    Endpoint for submitting user credentials.

Parameters:
    - username: Username of the user (string)
    - password: Password of the user (string)

Response:
    - 200 OK: Credentials submitted successfully
    - 400 Bad Request: Username already exists

View Passwords
--------------

URL: /view_passwords
Method: GET

Description:
    Endpoint for viewing saved passwords.

Response:
    - HTML page displaying a list of saved passwords

Contributing
============

We welcome contributions to the Flask project! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.

Please ensure that your code follows the project's coding standards and includes appropriate tests and documentation.

License
=======

The Flask project is licensed under the MIT License.

For more information, see the LICENSE file in the project repository.


