import requests
from lxml import html
import json

def name_check(name):
    titles = ['PhD', 'SM', 'MNG', 'PD']
    name = name.split()[1:]
    for i in reversed(range(len(name))): 
        if ("'" in name[i] and len(name[i]) == 3) or ("'" in name[i] and "," in name[i] and len(name[i]) == 4):
            del(name[i])
        elif name[i] in titles:
            del(name[i])
    return ' '.join(name)

url = 'https://www.example.com'
page = requests.get(url)
simplify_name = False

tree = html.fromstring(page.content)
names = tree.xpath('example-name-path')
emails = tree.xpath('example-email-path')


with open("emails.json", "w") as f:
    if simplify_name:
        out = {name_check(names[i]): emails[i] for i in range(len(names))}
    else:
        out = {names[i]: emails[i] for i in range(len(names))}
    print(f"Found {len(out)} name-email combinations")
    json.dump(out, f)