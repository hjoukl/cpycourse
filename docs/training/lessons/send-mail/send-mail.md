!!! question "Lesson: Email-4-You"

    === "Task"

        Send yourself an email!
        
        On program start ask the user to provide

        - an SMTP server address (the mail sender host)
        - email recipient domain name (e.g. `example.org`)

        Afterwards

        - get the username from the shell environment variable 'USERNAME'
          (Windows) or 'USER' (Linux) to prepare your recipient email address
        - create a connection to the mail host
        - send yourself an email with the subject "Hello from the Python 
          course" and the email body content "Currently working on ...", from a
          synthetic email sender address e.g. "test.test@python-course.de"

        Optional: Extend the program to allow email attachments. Ask the user
        to provide a filepath for the attachment.

        Expected result: Check your email account for the incoming email
        (optionally with attachment). An email with above sender, recipients,
        subject and message body should be there.

    === "Hints"

        - use `input()` built-in function to get user informations
        - use `os.environ` mapping object from the Python Standard Library, to
          read environment variables
        - use `smtplib.SMTP` class from the [smtplib](
          https://docs.python.org/3/library/smtplib.html) module of the Python
          Standard Library, to establish a connection to the mail server
        - alternatively, use `smtplib.SMTP_SSL` class for secure connections
          (e.g. if you want to try and access your mail providers SMTP server)
        - use the `STMP`object's `send_mail` method; you need to construct an
          appropriate `msg` argument, e.g. using f-strings:
          `msg = f'From: {sender}\nTo: {receiver}\nSubject: {subject}\n\n{payload}'`

        Optional:

        - use the `email.message.EmailMessage` class from the [email](
          https://docs.python.org/3/library/email.html) Python Standard Library
          module to create the email message.

    === "Solution"

        ??? pied-piper "Simple Python Email client"

            This example requires unauthenticated SMTP server access and a 
            local user name that is usable as E-Mail receiver.

            ``` python title="sendmail_compact.py"
            --8<-- "training/lessons/send-mail/sendmail_compact.py"
            ```

            [:material-file-download:](sendmail_compact.py)

            Such simple snippets typically also work well as shell one-liners:

            ``` console title="sendmail-compact.sh"
            --8<-- "training/lessons/send-mail/sendmail-compact.sh"
            ```
            
            ``` ps1con title="sendmail-compact.ps1"
            --8<-- "training/lessons/send-mail/sendmail-compact.ps1"
            ```

        ??? pied-piper "Simple Python TLS Email client"

            This example shows how to send an email with an SMTP server you
            can connect securely to using TLS, with your own username and
            password. I. e. your email provider of chooice e.g. Google Mail,
            GMX, mailbox.org, web.de, <...whatever...>  account.

            You need the SMTP server address of your mail provider and your
            credentials.

            ``` python title="sendmail_tls.py"
            --8<-- "training/lessons/send-mail/sendmail_tls.py"
            ```

            [:material-file-download:](sendmail_tls.py)

        ??? pied-piper "Python Email client using 'MailServer' class"

            This example requires unauthenticated SMTP server access and a 
            local user name that is usable as E-Mail receiver.

            ``` python title="sendmail.py"
            --8<-- "training/lessons/send-mail/sendmail.py"
            ```

            [:material-file-download:](sendmail.py)

            Such simple snippets typically also work well as shell one-liners:

            ``` console title="sendmail.sh"
            --8<-- "training/lessons/send-mail/sendmail.sh"
            ```
            
            ``` ps1con title="sendmail.ps1"
            --8<-- "training/lessons/send-mail/sendmail.ps1"
            ```


        ??? pied-piper "Python Email client enabled for email attachments"

            ``` python title="sendmail_with_attachment.py"
            --8<-- "training/lessons/send-mail/sendmail_with_attachment.py"
            ```

            [:material-file-download:](sendmail_with_attachment.py)
