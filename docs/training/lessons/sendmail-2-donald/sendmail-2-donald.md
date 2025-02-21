!!! question "Lesson: Email-2-Donald"

    === "Task"

        Send yourself an Email
        
        On program-start ask, the user to provide

        - Nickname

        Afterwards

        - get the username from the shell enivronment variable 'USERNAME' (Windows) or 'USER' (Linux) to prepare your email-address
        - create a connection to the mail-host 'smtp.freesmtpservers.com'
        - send an email to 'donald.duck@test.com with the subject "Hello from the Python-Course" and the content = "Currently working on ..." from a synthetic email sender-address e.g. "f{user}.{nickname}@pycource.com"  (Python f-string notation)

        Optional: Extend the program to allow email-attachments. For this ask the user to provide a filepath for the attachment.


        Expected result: Check your mail-inbox on th your sender-address at https://www.wpoven.com/tools/free-smtp-server-for-testing for the incoming email (opionally with attachment)

    === "Hints"

        - use `input()`-builtin function to get user nickname
        - use `os.environ`- mapping object from the Python Standard Library, to read environment variables
        - use `smtplib.SMTP`- class from the [smtplib](https://docs.python.org/3/library/smtplib.html) module of the Python Standard Library, to establish a connection to the mailserver
        - use f-string `msg = f'From: {sender}\nTo: {receiver}\nSubject: {subject}\n\n{payload}'`


    === "Solution"

        ??? pied-piper "Simple Python Email client"

            ``` python title="sendmail-2-donald.py"
            --8<-- "training/lessons/sendmail-2-donald/sendmail-2-donald.py"
            ```

