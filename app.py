from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import string
import hashlib

app = Flask(__name__)

# MongoDB Configuration
client = MongoClient("mongodb+srv://akashh2151:aOSefZ94SgQEkzmg@cluster0.25xmos0.mongodb.net/?retryWrites=true&w=majority")
db = client["emc_project"]
collection = db["signup"]

# SMTP Configuration
def send_email(subject, recipient, message):
    sender_email = "akashdesai2151@gmail.com"
    sender_password = "okhnsnnviavjfsej"
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient, msg.as_string())
    server.quit()

# Generate a reset token
def generate_reset_token(email):
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    collection.update_one(
        {"email": email},
        {"$set": {"reset_token": token}}
    )
    return token

@app.route('/reset_password', methods=['POST'])
def request_reset_password():
    data = request.json
    email = data.get('email')

    user = collection.find_one({"email": email})

    if user:
        token = generate_reset_token(email)
        reset_link = f"http://your-website.com/reset_password/{token}"  # Replace with your website URL
        message = f"Click the following link to reset your password: {reset_link}"
        
        send_email("Password Reset", email, message)
        return jsonify({"message": "Password reset link sent successfully"}), 200
    else:
        return jsonify({"message": "User not found"}), 404

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if request.method == 'GET':
        user = collection.find_one({"reset_token": token})

        if user: 
            # Render a password reset form for the user
            return render_template('reset_password.html', token=token)
        else:
            return jsonify({"message": "Invalid token"}), 404

    if request.method == 'POST':
        data = request.form
        token = data.get('token')
        password = data.get('password')

        user = collection.find_one({"reset_token": token})

        if user:
            # Hash the new password
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            
            # Update the user's password and remove the reset token
            collection.update_one(
                {"email": user["email"]},
                {"$set": {"password": hashed_password}, "$unset": {"reset_token": ""}}
            )
            return jsonify({"message": "Password reset successful"}), 200
        else:
            return jsonify({"message": "Invalid token"}), 404

if __name__ == '__main__':
    app.run(debug=True)
