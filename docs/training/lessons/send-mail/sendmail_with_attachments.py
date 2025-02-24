# sendmail_with_attachments.py

import mimetypes
import os
import smtplib
from email.message import EmailMessage


def username():
    """Return the local server OS user name.
    """
    if os.name == 'nt':
        user = os.environ['USERNAME']
    elif os.name == 'posix':
        user = os.environ['USER']
    return user


def mail_attachment_type(attachment):
    """Guess and return the mail attachment main and sub-type, as a tuple.
    """
    # Guess the content type based on the file's extension.
    content_type, encoding = mimetypes.guess_type(attachment)
    if content_type is None or encoding is not None:
        # No guess could be made, or the file is encoded (compressed), so
        # use a generic bag-of-bits type.
        content_type = 'application/octet-stream'
    maintype, subtype = content_type.split('/', 1)
    return (maintype, subtype)


class MailServer:
    def __init__(self, smtp_host):
        self.mail_server_name = smtp_host
        self.mailserver = smtplib.SMTP(smtp_host)
        #self.mailserver.set_debuglevel(1)

    def __del__(self):
        if self.mailserver:
            self.mailserver.quit()

    def _attach(self, email, attachment):
        maintype, subtype = mail_attachment_type(attachment)
        with open(attachment, 'rb') as fp:
            email.add_attachment(
                fp.read(), maintype=maintype, subtype=subtype,
                filename=os.path.basename(attachment),
                )

    def send_mail_with_attachment(
            self, sender, receivers, subject, content, attachment=None
            ):
        """Send mail with attachment.
        """
        # https://docs.python.org/3/library/email.examples.html

        # Prepare message, build using EmailMessage
        email = EmailMessage()
        email['Subject'] = subject
        email['From'] = sender
        email['To'] = ','.join(receivers)
        email.set_content(content)
        self._attach(email, attachment)

        self.mailserver.send_message(email)


def main():
    try:
        # Ask for mail server address.
        smtp_host = input("SMTP Host: ")
        domain_name = input("E-mail domain name: ")
        file_path = input("Attachment file path: ")

        user = username()

        sender = 'test.test@python-course.de'
        subject = 'Python Course Test SMTP-Email'
        msg_payload = 'Currently working on something very important.'
        receiver = f"{user}@{domain_name}"
        receivers = [receiver] # must be a list

        mailServer= MailServer(smtp_host)
        mailServer.send_mail_with_attachment(
            sender, receivers, subject, msg_payload, file_path)

    except Exception as exc:
        print(f'ERROR: {str(exc)}')


if __name__ == '__main__':
    main()
