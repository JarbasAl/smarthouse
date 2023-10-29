from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL


def send_smtp(user, pswd, sender,
              destinatary, subject, contents,
              host, port=465):
    with SMTP_SSL(host=host, port=port) as server:
        server.login(user, pswd)
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = destinatary
        msg['Subject'] = subject
        msg.attach(MIMEText(contents))
        server.sendmail(sender, destinatary, msg.as_string())


if __name__ == "__main__":
    with open("report.txt") as f:
        report = f.read()

    print(report)

    user = ""
    pswd = ""
    host = "smtp.mailfence.com"
    port = 465

    subject = "Price Report"
    body = report
    recipient = ""

    send_smtp(user, pswd,
              user, recipient,
              subject, body,
              host, port)
