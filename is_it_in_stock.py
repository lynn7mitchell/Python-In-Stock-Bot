from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import smtplib
from email.message import EmailMessage
from login import email_to, email_from, email_from_password


email = EmailMessage()
email['from'] = 'Python In Stock Bot'
email['to'] = email_to
email['subject'] = 'Get Freaky Zone Is In Stock!'

driver = webdriver.Chrome()
url = driver.command_executor._url

driver.get("https://foundationdiscs.com/products/get-freaky-zone?_pos=1&_psq=get-frea&_ss=e&_v=1.0")

print(driver.find_element_by_class_name('add-to-cart').is_enabled())

while(not driver.find_element_by_class_name('add-to-cart').is_enabled()):
    print('not in stock')
    time.sleep(1)
    driver.refresh(30);
    


print('in stock')

email.set_content('This get freaky zone is in stock! https://foundationdiscs.com/products/get-freaky-zone?_pos=1&_psq=get-frea&_ss=e&_v=1.0')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # start server
    smtp.ehlo()
    # ttls is encryption
    smtp.starttls()
    # dummy email
    smtp.login(email_from, email_from_password)
    smtp.send_message(email)
    print('it worked')