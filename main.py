import smtplib
import datetime as dt
import random

my_email = "<email adress you want to send mails from"
my_password = "<app password for the mail ID>"

now = dt.datetime.now()
weekday = now.weekday()
if weekday ==0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("<SMMTP adress for the mail ID you are sending mails from>") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="<mail_ID you want to send mails to>",
                            msg=f"Subject: Monday Motivation \n\n {quote}")
