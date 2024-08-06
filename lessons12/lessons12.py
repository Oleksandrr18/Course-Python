import re
woulds = 'Rbbr, RBRr, Rbr, Rbbbr, and another example Rr'

r = re.findall('R[bB]+r', woulds)
print(r)
# task 3
import re
def is_valid_email(email):
    ex = r'^[A-Za-z0-9]+([_\-][A-Za-z0-9]+)*@[A-Za-z0-9]+\.[com]'
    return re.match(ex, email) is not None



emails = [
    'indexupl@gmail.com',
    'indexx.upl@gmail.com',
    'indeeeeex.upl@gmail.com',
    'indexx.upl@giiimail.com',
    'indexx+upl@gmail.com',

]

for email in emails:
    print(f'{email}: {is_valid_email(email)}')

# task 4
import re
def login(log):
    ex = r'^[A-Za-z0-9]{2,10}$'
    return re.match(ex, log) is not None

logins = [
    'user66',
    'user65765765765',
    'user09'
]
for log in logins:
    print(f'{log}: {login(log)}')

