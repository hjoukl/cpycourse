# -*- coding: utf-8 -*-
# sendmail_2_donald.py

# Use free smtp-server
# https://www.wpoven.com/tools/free-smtp-server-for-testing
# server: smtp.freesmtpservers.com
# port: 25

import os
import smtplib


def username():
    """Return the local server OS user name.
    """
    if os.name == 'nt':
        user = os.environ['USERNAME']
    elif os.name == 'posix':
        user = os.environ['USER']
    return user


class MailServer:
    def __init__(self, smtp_host, port=25):
        self.mailserver = smtplib.SMTP(smtp_host, port=port)
        #self.mailserver.set_debuglevel(1)

    def __del__(self):
        try:
            self.mailserver.quit()
        except:
            pass

    def send_mail(self, sender, receivers, subject, content=''):
        """Send an email message from sender address `sender`to recipients in 
        `receivers`.
        """
        receivers_str = ', '.join(receivers)
        # NOTE: Need this special format! see help(smtplib.SMTP.sendmail)
        msg = (
            f'From: From Person {sender}\n'
            f'To: {receivers_str}\n'
            f'Subject: {subject}\n\n'
            f'{content}'
            )
        print(f'\nEmail:\n<<<\n{msg}\n>>>\n')

        self.mailserver.sendmail(sender, receivers, msg)


def main():
    try:
        smtp_host = 'smtp.freesmtpservers.com'

        # Ask for nickname to compose the sender email-address
        nickname = input('Please provide your nickname: ')
        # Get user to compose the sender email address from environment.
        user = username()

        sender = f'{user}.{nickname}@pycourse.com'

        subject = 'Python-Course Test SMTP-Email'
        msg_payload = 'Currently working on something very important.'
        receiver = 'donald.duck@test.com'
        receivers = [receiver] # must be a list

        mail_server = MailServer(smtp_host)
        mail_server.send_mail(sender, receivers, subject, msg_payload)

        print(
            f'Check inbox at '
            f'https://www.wpoven.com/tools/free-smtp-server-for-testing for '
            f'mail (with receiver {receiver} or sender {sender} address)'
            )
        del mail_server  # For illustration purposes - goes out of scope anyway

    except Exception as e:
        print(f'ERROR: {str(e)}')


if __name__ == '__main__':
    main()
