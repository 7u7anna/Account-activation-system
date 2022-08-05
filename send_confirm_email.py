from email.message import EmailMessage
import os
import smtplib

def sendEmail(user_mail):
    EMAIL_ADDRESS = os.environ.get(EMAIL_ADDRESS)
    EMAIL_PASSWORD = os.environ.get(EMAIL_PASSWORD)

    email = EmailMessage()
    email['Subject'] = 'Account have been created successfully'
    email['To'] = str(user_mail)
    email['From'] = EMAIL_ADDRESS
    email.set_content(
        'Your account have been created!\nThank you for choosing our platform\n\nKind Regards,\nOur Team'
    )

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(email)
