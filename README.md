# Python In Stock Bot

This is a script I built to practice programming in Python. This script will refresh the product page on foundationdiscs.com for a disc called the 'Get Freaky FLX Zone' and check to see if the button, that displays either 'Sold Out' or 'Add To Cart', is active or not. If the button is active then it will send me an email letting me know that the disc is in stock. This script is meant to let me know that the disc is in stock and will not buy the disc on it's own. 

## How To Use This Script

1. Clone This Repo
2. Pip install selenium
3. Create a file called 'login.py'
4. In login.py set variables for email_to, email_from, and email_from_password
5. Set email_to to the email that will receive the update that the disc is in stock.
6. Set email_from to the secondary email that the update will be sent from.
7. Set email_from_password to the password for the secondary email that the update will be sent from
8. Run py -3 is_it_in_stock.py
