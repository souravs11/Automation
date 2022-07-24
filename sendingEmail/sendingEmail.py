###
# Target Release:       1.0
# Code Status:          Complete
# Code Developer:       Sourav
# Script Name:          sendingEmail.py
# How to run:           python3 sendingEmail.py
###

# Import Libraries/Modules
import smtplib                              # This module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon.
import ssl                                  # This module provides access to Transport Layer Security (often known as “Secure Sockets Layer”) encryption and peer authentication facilities for network sockets, both client-side and server-side.
from email.message import EmailMessage      # EmailMessage provides the core functionality for setting and querying header fields, for accessing message bodies, and for creating or modifying structured messages.

# Defining email components
subject = "SUBJECT_GOES_HERE"
body = "MESSAGE_BODY_GOES_HERE"
sender_email = "SENDER_EMAIL_GOES_HERE"
receiver_email = "RECEIVER_EMAIL_GOES_HERE"
password = input("Enter a password: ")

# Formatting the message components using EmailMessage
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["subject"] = subject
message.set_content(body)

# Alternatively the following HTML block can be used to send better-formatted email.
html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""
message.add_alternative(html, subtype="html")   # Because we will be sending email message formatted in HTML

context = ssl.create_default_context()          # SSL will be used for secure email transfer

# Sending Email . . .
print(f'Sending Email . . .')

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:    # Connecting to Gmail's SMTP server
    server.login(sender_email, password)                                    # Logging into the sever
    server.sendmail(sender_email, receiver_email, message.as_string())      # Sending the email as a string

print(f'Message sent successfully!')