
from jira import JIRA

options = {'server': 'https://jira.bgelov.ru'}
jira = JIRA(options, basic_auth=('testjira', '******Password******'))
issue = jira.issue('GSE-5125')
print(issue.fields.reporter.name)
