# Python Notification Sender Script #
This Python script sends notification emails using the Simple Mail Transfer Protocol (SMTP) and MIME (Multipurpose Internet Mail Extensions). The script is capable of sending plain text messages as well as including image attachments in the emails. 
It is designed to work with Gmail, but it can be modified to use other email providers.

# In the Works #
Currently working on functionality to schedule when emails are sent. This will enable the script to be used as a useful reminder tool

# Features #
- Send notification emails via SMTP
- Supports sending plain text emails.
- Optionally includes image attachments in the email.
- Securely connects to the SMTP server using SSL/TLS.
# Prerequisites #
- Python 3.x
- A Gmail account with "App Password" enabled
- Required Python packages:
- smtplib
- ssl
- os
