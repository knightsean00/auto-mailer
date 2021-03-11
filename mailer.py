import os
import win32com.client as w
import json

# your_name as it appears on the sheet and will appear on the email
your_name = ''
cc_email = ''
signature = ''
auto_send = False

with open('emails.json', 'r') as f:
    emails = json.load(f)

outlook = w.Dispatch('outlook.application')

for name, email in emails.items():

    print(f"\nStarting {name}'s email")

    msg = outlook.CreateItem(0)
    msg.To = str(email)

    if (cc_email):
        msg.CC = cc_email

    msg.Subject = f"Auto-email to {name}"
    msg.HTMLBody = (
        f"""Dear {name},<br><br>
        My name is {your_name}, you have been auto-emailed!<br><br>
        {signature},<br>
        {your_name}
        """)

    if auto_send:
        msg.Send()
    else:
        msg.Display(True)

print("Finished!")