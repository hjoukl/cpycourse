# -*- coding: utf-8 -*-
import os
import smtplib
import sys

# Use free smtp-server
# https://www.wpoven.com/tools/free-smtp-server-for-testing
# server: smtp.freesmtpservers.com
# port: 25

class MailServer:
    def __init__(self, smtp_host, port=25):
        self.mailserver = smtplib.SMTP(smtp_host, port=port)
        #self.mailserver.set_debuglevel(1)

    def __del__(self):
        if self.mailserver:
            self.mailserver.quit()

    def send_mail(self, sender, receivers, msg):
        ''' send a pre-formatted' message '''
        self.mailserver.sendmail(sender, receivers, msg)

def main():
    try:
        SMTP_HOST = 'smtp.freesmtpservers.com'

        # Ask for nickname to compose the sender email-address
        nickname = input('Please provid your nickname: ')

        # Ask for User to build sender email-adress
        if os.name == 'nt':
            user = os.environ['USERNAME']
        elif os.name == 'posix':
            user = os.environ['USER']

        sender = f'{user}.{nickname}@pycourse.com'

        subject = 'Python-Course Test SMTP-Email'
        msg_payload= 'This is a test Email.'
        receiver = f'donald.duck@test.com'
        receivers = [receiver] # must be a list

        # NOTE: Need this special format! see help(smtplib.SMTP.sendmail)
        #msg = f'From: From Person {sender}\nTo: {receiver}\nSubject: {subject}\n\n{msg_payload}'
        msg = (
            f'From: From Person {sender}\n'
            f'To: {receiver}\n'
            f'Subject: {subject}\n\n'
            f'{msg_payload}'
            )

        print(f'\nEmail\n<<<\n{msg}\n>>>\n')

        mailServer= MailServer(SMTP_HOST)

        # # Provide a pre-formatted message 'msg'
        mailServer.send_mail(sender, receivers, msg)

        del mailServer

    except Exception as e:
        print(f'ERROR: {str(e)}')

if __name__ == '__main__':
    main()
