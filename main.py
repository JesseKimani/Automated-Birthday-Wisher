import smtplib
import random
from datetime import datetime
import pandas


today = datetime.now()
today_tuple = (today.month, today.day)

my_email = "jesse@gmail.com"
password = "mrjpxkwewjootmnc"

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        new_letter = contents.replace("[NAME]", birthday_person["name"])

# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

    connection = smtplib.SMTP_SSL("smtp.gmail.com", port=465, timeout=10)
    connection.login(user=my_email, password=password)

    connection.sendmail(
        from_addr=my_email,
        to_addrs=birthday_person["email"],
        msg=f"Subject:Happy Birthday \n\n{new_letter}"
    )
    connection.close()
