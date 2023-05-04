import smtplib

from email.message import EmailMessage

import ssl  # for faster bulk-mail delivery

# COLLECT USER INFO
Name = input('Name: ABIODUN')
sender = input('Sender email: ogunbanwoabiodun@gmail.com')
recipient = input('Recipient emails : tanimola32@gmail.com').split(',')
mypassword = 'ygbmnizbpuyaibrg'
subject = input('Subject: EMAIL TESTING RUNNING')
body = input('email body content: This is my first email test ruuning project in python')


# CREATE THE OBJECT OF THE EMAIL CLASS, EMAILMESSAGE ;
email_me = EmailMessage()

email_me['Subject'] = subject
email_me['From'] = sender
email_me['To'] = ','.join(recipient)
email_me.set_content(body)

context = ssl.create_default_context()

# OPENNING THE CONNECTION TO GMAIL SERVER AND SEND MESSAGE
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as mailme:
    mailme.login(sender, mypassword)
    mailme.sendmail(sender, recipient, email_me.as_string())
    # mailme.send_message(email_me)

    print('email sent successfully!')
