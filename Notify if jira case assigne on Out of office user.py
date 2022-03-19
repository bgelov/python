#Notify if jira case assigne on Out of office user
#this script mapped on event when Jira send message to users from Out of office group

import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jira import JIRA


def get_reporter(case_key):
    options = {'server': 'https://jira.bgelov.ru'}
    jira = JIRA(options, basic_auth=('tasksuser', '********password********'))
    issue = jira.issue(case_key)
    reporter_login = issue.fields.reporter.name
    assignee_login = issue.fields.assignee.name
    assignee_displayName = issue.fields.assignee.displayName
    send_notif(assignee_login,assignee_displayName,case_key)

def send_notif(assignee_login,assignee_displayName,case_key):
    TO = assignee_login + '@bgelov.ru'
    msg = MIMEMultipart('alternative')
    msg['Subject'] = case_key + ' назначен на сотрудника с автоотбивкой в почте'
    msg['From'] = 'JIRA Out Of Office <JIRA-ooo@bgelov.ru>'
    msg['To'] = TO

    html = """\
    <html>
    <head></head>
    <body>
        <p>Вероятно, {0} недоступен или в отпуске.<br>
        Ссылка на задачу: <a href="https://jira.bgelov.ru/browse/{1}">{1}</a>
        </p>
    </body>
    </html>
    """.format(assignee_displayName,case_key)

    part = MIMEText(html, 'html')
    msg.attach(part)
    s = smtplib.SMTP('smtp.bgelov.ru')
    s.send_message(msg)
    s.quit()

 
if len(sys.argv) != 2:
    raise ValueError('Не передан GSE-number.')
else:
    get_reporter( sys.argv[1])