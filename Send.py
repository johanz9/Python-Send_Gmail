import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from_address = "name@gmail.com"
to_address = "name@gmail.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Urgente! da leggere subito!\n\n"
msg['From'] = from_address
msg["To"] = to_address

# Create the message (HTML).

html = """\

We are sending an email using Python and Gmail, how fun! We can fill this with html, and gmail supports a decent range of css style attributes too - https://developers.google.com/gmail/design/css#example.

"""

# Record the MIME type - text/html.
part1 = MIMEText(html, 'html')

# Attach parts into message container
msg.attach(part1)

# Credentials
username = 'username@gmail.com'
password = 'App Password'


#Connect to the Server
email = smtplib.SMTP("smtp.gmail.com", 587)
email.ehlo()

#Channel Crypted
email.starttls()

#login
Error = 1
while Error == 1:
    try:
        print("Starting Login")
        email.login(username, password)
        Error = 0
        print("Succefully Login")
    except:
        print("Username Or Password aren't Correct")
        print(""" Be sure to use App password from Google. More information  \
https://support.google.com/accounts/answer/185833?p=InvalidSecondFactor&visit_id=637276493567303700-236054552&rd=1)
        """)
        print("Enter Again the Username and Password: ")
        username = input("Enter Username (example@gmail.com) :")
        password = input("Enter Password: ")


#send the message
email.sendmail(from_address,to_address,msg.as_string())

#Close connection
email.quit()