# sendmail_compact.py

# Note: This only works for unauthenticated SMTP. The local username (i.e.
# $USER on Unix) must be usable as a mail sender and recipient address.
#
import os
import smtplib


def main():
    try:
        # Ask for mail-server
        smtp_host = input("SMTP host: ")
        domain_name = input("E-Mail domain name: ")

        if os.name == 'nt':
            user = os.environ['USERNAME']
        elif os.name == 'posix':
            user = os.environ['USER']

        sender = 'test.test@python-course.de'
        subject = 'Python Course Test SMTP E-Mail'
        msg_payload= 'This is a test E-Mail.'
        receiver = f"{user}@{domain_name}" 
        receivers = [receiver] # must be a list

        # NOTE: Pre-formatted message:
        # NOTE: Need this special format! see help()
        msg = (
            f'From: From Person {sender}\nTo: {", ".join(receivers)}'
            f'\nSubject: {subject}\n\n{msg_payload}'
            )

        print(f'\nEmail\n<<<\n{msg}\n>>>\n')

        mail_server = smtplib.SMTP(smtp_host)
        mail_server.sendmail(sender, receivers, msg)

    except Exception as e:
        print(f'ERROR: {str(e)}')


if __name__ == '__main__':
    main()
