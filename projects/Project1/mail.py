import smtplib
try:
    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.starttls()
    reciever_email=input("enter your email = ")
    sender_email="rizwanali0294@gmail.com"
    passwd="maqc wpmv ypbk hytb"
    server.login(sender_email,password=passwd)
    subject=input("what's your problem")
    body=input("tell me the details")
    message=f"subject {subject}\n\n{body}"
    server.sendmail(sender_email,reciever_email,message)
    print("send &%")
    server.quit()
except Exception as e:
    print(e)

else:
    print("yes we did it ")

finally:
    print("here we go ")