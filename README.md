# auto-mailer

Basically just a auto-emailer/crawler that I made to mass email MIT staff. I'm just pushing this because I will probably use this again in the future.

## Crawling
Run `py email_crawl.py` with the parameters specified in the file to get all the email-name combinations found as a pattern on one particular page (note: crawler does not go past provided page)

## Emailing
Uses Microsoft Outlook and will repeatedely open up new messages that will auto-fill for fast sending. `auto_send` flag automatically sends the email if set to `True`, otherwise, the message will open up so that you can preview it before it is sent.