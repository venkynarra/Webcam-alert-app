import smtplib
import imghdr

from email.message import EmailMessage
PASSWORD = "gxenzaeklfhsxvuk"
SENDER = "venkateshnarra368@gmail.com"
RECEIVER = "venkateshnarra368@gmail.com"
def send_email(image_path):
    print(f"Preparing email for: {image_path}")  # ADD
    email_message = EmailMessage()
    email_message["Subject"] = "New Customer showed up"
    email_message.set_content("Hey, we just saw a new customer")

    try:
        with open(image_path, 'rb') as file:
            content = file.read()
        email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

        gmail = smtplib.SMTP("smtp.gmail.com", 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(SENDER, PASSWORD)
        gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
        gmail.quit()
        print(f"✅ Email sent with image: {image_path}")

    except Exception as e:
        print(f"❌ Failed to send email: {e}")
if __name__ == "__main__":
    send_email("images/10.png")
