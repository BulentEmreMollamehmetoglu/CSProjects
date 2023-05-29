import smtplib

def send_email(email,password,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()


# new email -->
send_email("cyberheresec@gmail.com","btapydlbtadqldyg","hello there")
