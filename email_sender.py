import smtplib, ssl

port = 465
receiver_email = "@gmail.com"
sender_email = "@gmail.com" #input("Type sending email: ")
password = "" #input("Type your password: ")
message = """Subject: Hi there
This message is sent from Python.""" #use "Subject:" to set a subject

context = ssl.create_default_context()

#with will make sure your connection is closed afterward

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)