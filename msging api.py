import smtplib
from email.message import EmailMessage
def email(sub,b,to):
    msg=EmailMessage()
    msg.set_content(b)
    msg['subject']=sub
    msg['to']=to
    

    user="anmeshgpt@gmail.com"
    msg['from']=user
    password="roimquwvhhoeuzcy"

    server =smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()
    print(msg)
if __name__=='__main__':
    email("Hey","Hi Aastha Sharma \n This is to inform you about the penalty that have been imposed on you because of violation of national traffic rules.\n You are liable to pay Rs. 500 for the same. Please make sure you do not contravene any of the traffic rules.\n Regards,\n Crossroad Corps Team","sharmaastha766@gmail.com")

