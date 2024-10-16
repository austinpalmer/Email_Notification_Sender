import smtplib, ssl, os
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def create_image_attachment(path: str) -> MIMEImage:
    """
    Reads the image path, converts bytes to a MIMEImage

    :param path:

    :return: mime_image
    """
    with open(path, 'rb') as image:
        mime_image = MIMEImage(image.read())
        mime_image.add_header('Content-Disposition', f"attachment; filename={path}")
        return mime_image

def send_email(to_email: str, subject: str, body: str, image: str | None = None):
    """
    Creates and sends an email based on the user
    input using Simple Mail Transfer Protocol (SMTP).

    :param to_email:
    :param subject:
    :param body:
    :param image:

    """
    host: str = "smtp.gmail.com"
    port: int = 587

    # Establish a server to securely start an email session and login
    context = ssl.create_default_context()
    with smtplib.SMTP(host, port) as server:
        print("Logging in...")
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(os.getenv("EMAIL"), os.getenv("PASSWORD"))

        # Prepare the email
        print("Attempting to send email.")
        message = MIMEMultipart()
        message["From"] = os.getenv("EMAIL")
        message["To"] = to_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        if image:
            file: MIMEImage = create_image_attachment(image)
            message.attach(file)

        server.sendmail(from_addr=os.getenv("EMAIL"), to_addrs=to_email, msg=message.as_string())
        print("Sent email.")

def main():
    message: str = "Hello my love, this is a test email sent from my python program."
    send_email(to_email="peacefulvictory2002@gmail.com",
               subject="Testing",
               body=message)

if __name__ == "__main__":
    main()