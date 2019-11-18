"""
    The main class used to send mail to the required user.
"""
import smtplib

mail_text = """
            Hi {},

  I am LISA - Learning Intelligent and Sharing Assistant of Kris. The sole purpose of my existence is to share what Kris learns every day with like-minded people like yourself. Everyday Kris reads multiple articles, watched numerous videos and most of the time he thinks to share the same with others but doesn't. So I took the responsibility of the looking through what he bookmarks and through some creative decision process understand what he tries to learn and share it with others so that they too can benefit from the knowledge and save a lot of time in the process. 
  Presently I am on an automated mode to run once a day and share if anything is interesting that might be suited for you. Here are some articles for today  
        
"""

email_details = [
    {
        'name': 'Rens',
        'email': 'rens@kimo.ai'
    },
    {
        'name': 'Obrian',
        'email': 'obrian@kimo.ai'
    }
]

tmp_details = [
    {
        'name': 'Krishna',
        'email': 'krishna@kimo.ai'
    }
]

sender_email_id = 'info@criativo.ai'
sender_email_id_pass = 'Inf0#1985'

s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login("sender_email_id", "sender_email_id_password")
for person in tmp_details: 
    message = mail_text.format(person['name'])
    s.sendmail("sender_email_id", person['email'], message) 
s.quit()