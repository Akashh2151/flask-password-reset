Password Reset Application with Flask and MongoDB

This is a Flask-based web application that allows users to request a password reset and reset their password using a unique token sent to their email address. It uses MongoDB for user data storage and sends reset emails via SMTP.

Features
Password Reset Request: Users can request a password reset by providing their email address.
Email Notification: Upon request, an email with a unique reset link is sent to the user's email address.
Password Reset: Users can reset their password by clicking the link in the email and providing a new password.
Security: Passwords are securely hashed before storage, and unique reset tokens are generated for each request.
Prerequisites
Before running the application, make sure you have the following:

Python 3.x installed
Flask framework installed
MongoDB set up with a collection named signup
Gmail account credentials for sending emails (you may consider using environment variables for sensitive data)
Getting Started

1 Clone the repository to your local machine:

git clone https://github.com/akashh2151/flask-password-reset.git

2 Install the required Python packages:

pip install Flask pymongo


3 Configure MongoDB:

Set up a MongoDB database and collection.
Update the MongoDB URI in the client initialization in the code to point to your database.

4 Configure SMTP for Email Notifications:

Replace sender_email and sender_password with your Gmail account credentials.
Make sure to enable "Less secure apps" in your Gmail settings.

5 run the application

python app.py

The application will be running at http://localhost:5000.



Password Reset Application with Flask and MongoDB
This is a Flask-based web application that allows users to request a password reset and reset their password using a unique token sent to their email address. It uses MongoDB for user data storage and sends reset emails via SMTP.

Features
Password Reset Request: Users can request a password reset by providing their email address.
Email Notification: Upon request, an email with a unique reset link is sent to the user's email address.
Password Reset: Users can reset their password by clicking the link in the email and providing a new password.
Security: Passwords are securely hashed before storage, and unique reset tokens are generated for each request.
Prerequisites
Before running the application, make sure you have the following:

Python 3.x installed
Flask framework installed
MongoDB set up with a collection named signup
Gmail account credentials for sending emails (you may consider using environment variables for sensitive data)
Getting Started
Clone the repository to your local machine:

shell
Copy code
git clone https://github.com/yourusername/your-repo.git
Install the required Python packages:

shell
Copy code
pip install Flask pymongo
Configure MongoDB:

Set up a MongoDB database and collection.
Update the MongoDB URI in the client initialization in the code to point to your database.
Configure SMTP for Email Notifications:

Replace sender_email and sender_password with your Gmail account credentials.
Make sure to enable "Less secure apps" in your Gmail settings.
Run the application:

shell
Copy code
python app.py
The application will be running at http://localhost:5000.

Usage
Request Password Reset
To request a password reset, make a POST request to /reset_password with a JSON payload containing the user's email address:
json
{
  "email": "user@example.com"
}


Password Reset Email
Upon a successful request, the user will receive an email with a unique reset link. The email will contain a link like this:

perl
Click the following link to reset your password: http://your-website.com/reset_password/token


Reset Password
1 Users can click the reset link in the email to access the password reset form.

2 Enter a new password and submit the form.

3 The application will securely hash the new password and update it in the database.

Customization
Replace http://your-website.com with your actual website URL in the reset_link variable in request_reset_password function.


Security Considerations
Passwords are securely hashed using SHA-256 before storage.
Reset tokens are unique for each user request.
Ensure that sensitive credentials (e.g., MongoDB URI, email credentials) are stored securely, such as using environment variables.
Contributions
Contributions are welcome! If you have any ideas for improvements or new features, feel free to submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.