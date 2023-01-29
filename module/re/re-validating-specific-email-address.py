#https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem

import re

def fun(s):
    # return True if s is a valid email, else return False
    # this email patterny only for this task!!!
    pattern = re.compile(r'([a-zA-Z0-9]+[_-])*[a-zA-Z0-9_-]+@[a-zA-Z0-9]+(\.[A-Z|a-z]{2,3})+')
    if re.fullmatch(pattern, s):
        return True
    else:
        return False

    
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)