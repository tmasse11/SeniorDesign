from googlevoice import Voice 
from googlevoice.util import input

sms = Voice()


username = 'trrllmassey@gmail.com'
password = '350zTm123+Tman13786++=='


sms.login(username,password)

phoneNumber = input('input the destination phone number.\t')
text = input('enter the text you wish to send\t')


sms.send_sms(phoneNumber,text)

