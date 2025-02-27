# sendmail_tls.py

import getpass
import smtplib


def main():
    try:
        # Ask for the mail server address.
        smtp_host = input('smtp server host: ')
        # Ask for the mail provider SMTP user name.
        smtp_username = input('smtp server username: ')
        # Use getpass() to not leak the password to the console.
        smtp_password = getpass.getpass('smtp server password: ')
        # Get the mail sender address. This is usually restricted to an address
        # that is under your account's control.
        sender =  input('sender email address: ')
        # Find out who this mail should be sent to.
        recipient =  input('recipient email address: ')

        subject = 'Python Course Test SMTP Email'
        msg_payload= 'This is a test email.'
        receivers = [recipient] # must be a list

        # NOTE: pre-formatted message!
        msg = (
            f'From: From Person {sender}\nTo: {receivers}\nSubject: {subject}'
            f'\n\n{msg_payload}'
            )

        print(f'\nEmail\n<<<\n{msg}\n>>>\n')

        # Use TLS for a secure connection.
        smtp = smtplib.SMTP_SSL(smtp_host)
        # Log in with your user credentials.
        smtp.login(smtp_username, smtp_password)
        # Sendt the mail out to the world (eh, the receivers).
        smtp.sendmail(sender, receivers, msg)

    except Exception as e:
        print(f'ERROR: {str(e)}')


if __name__ == '__main__':
    main()



