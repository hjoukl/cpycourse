!!! question "Lesson: Email-2-Donald"

    === "Task"

        Send an email to Donald!

        No, not *that* Donald.

        At program start ask the user to provide

        - a nickname

        Afterwards

        - get the username from the shell environment variable
          'USERNAME' (Windows) or 'USER' (Linux) to prepare your
          email-address
        - create a connection to the SMTP mail host
          `smtp.freesmtpservers.com`
        - send an email to 'donald.duck@test.com with the subject "Hello from
          the Python Course" and the content "Currently working on ..." from a
          synthetic email sender address (e.g.
          `f"{user}.{nickname}@pycourse.com"` (Python f-string notation))

        Expected result: Run the program, provide the required input and check
        the mail inbox at
        https://www.wpoven.com/tools/free-smtp-server-for-testing for the
        email. You can use either the sending or the receiving address to
        access the inbox.

        Optional: Extend the program to allow email attachments. Ask the user
        to provide a filepath for the attachment.

    === "Hints"

        - use the `input()` built-in function to get a user nickname
        - use `os.environ` from the Python Standard Library to read environment
          variables
        - use the `smtplib.SMTP`- class from the [smtplib](
          https://docs.python.org/3/library/smtplib.html) Python Standard
          Library module, to establish a connection to the mail server
        - use the `STMP`object's `send_mail` method; you need to construct an
          appropriate `msg` argument, e.g. using f-strings:
          `msg = f'From: {sender}\nTo: {receiver}\nSubject: {subject}\n\n{payload}'`

    === "Solution"

        ??? pied-piper "Simple Python Free SMTP Server Email Client"

            ``` python title="sendmail_2_donald.py"
            --8<-- "training/lessons/sendmail-2-donald/sendmail_2_donald.py"
            ```

            [:material-file-download:](sendmail_2_donald.py)
