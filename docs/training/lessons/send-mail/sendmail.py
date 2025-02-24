# sendmail.py
#
import os
import smtplib


class MailServer:
    def __init__(self, smtp_host):
        self.mailserver = smtplib.SMTP(smtp_host)
        #self.mailserver.set_debuglevel(1)

    def __del__(self):
        if self.mailserver:
            self.mailserver.quit()

    def send_mail(
            self, sender, receivers, subject, content
            ):
        """Send an email message from sender address `sender`to recipients in 
        `receivers`.
        """
        # NOTE: Pre-formatted message:
        # NOTE: Need this special format! see help()
        msg = (
            f'From: From Person {sender}\nTo: {", ".join(receivers)}'
            f'\nSubject: {subject}\n\n{content}'
            )

        print(f'\nEmail\n<<<\n{msg}\n>>>\n')
        self.mailserver.sendmail(sender, receivers, msg)


def username():
    """Return the local server OS user name.
    """
    if os.name == 'nt':
        user = os.environ['USERNAME']
    elif os.name == 'posix':
        user = os.environ['USER']
    return user


def main():
    try:
        smtp_host = input("SMTP host: ")
        domain_name = input("E-Mail domain name: ")

        user = username()
        sender = 'test.test@python-course.de'
        subject = 'Python Course Test SMTP E-Mail'
        msg_payload = 'Currently working on something very important.'
        receiver = f"{user}@{domain_name}"
        receivers = [receiver] # must be a list

        mailServer= MailServer(smtp_host)
        mailServer.send_mail(
            sender, receivers, subject=subject, content=msg_payload)

    except Exception as e:
        print(f'ERROR: {str(e)}')


if __name__ == '__main__':
    main()
