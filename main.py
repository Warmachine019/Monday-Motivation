import smtplib
import datetime as dt
import random

my_email = "spandantest12@gmail.com"
my_password = "meaj qsab pxlh pxag"

now = dt.datetime.now()
weekday = now.weekday()
if weekday ==0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="spandan019@gmail.com",
                            msg=f"Subject: Monday Motivation \n\n {quote}")