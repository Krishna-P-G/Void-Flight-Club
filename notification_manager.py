from sinch import Client
import smtplib
from config import my_email, password
my_email = my_email
password = password


class NotificationManager:

    def send_emails(self, emails, names, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            for name, email in zip(names, emails):
                connection.sendmail(from_addr=my_email,
                                    to_addrs=email,
                                    msg=f"Subject:Hey {name}, Here's the best flight deal for you!\n\n{message}")
                print(f"Email sent to {email}")