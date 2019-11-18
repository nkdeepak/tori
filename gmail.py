from __future__ import print_function
from googleapiclient.discovery import build
from apiclient import errors
from httplib2 import Http
from email.mime.text import MIMEText
import base64
from google.oauth2 import service_account

# Email variables. Modify this!
EMAIL_FROM = 'info@criativo.ai'
user_details = [
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
    },
    {
        'name': 'Deepak',
        'email': 'deepaknk@aditya.ac.in'
    }
]
#EMAIL_TO = ['Krishna@kimo.ai', 'obrian@kimo.ai', 'rens@kimo.ai']
#TEST_EMAIL_TO = ['krishna@kimo.ai', 'deepaknk@aditya.ac.in'] 
EMAIL_SUBJECT = 'Hello  from LISA !'
EMAIL_CONTENT = 'Hello, this is a test\nLyfepedia\nhttps://lyfepedia.com'
into_mail_template = """
            Hi {},

  I am LISA - Learning Intelligent and Sharing Assistant of Kris. The sole purpose of my existence is to share what Kris learns every day with like-minded people like yourself. Everyday Kris reads multiple articles, watched numerous videos and most of the time he thinks to share the same with others but doesn't. So I took the responsibility of the looking through what he bookmarks and through some creative decision process understand what he tries to learn and share it with others so that they too can benefit from the knowledge and save a lot of time in the process. 
  Presently I am on an automated mode to run once a day and share if anything is interesting that might be suited for you. Here are some articles for today  
        
"""

##################

def create_message(sender, to, subject, message_text):
  """Create a message for an email.
  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.
  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEText(message_text, 'html')
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

def send_message(service, user_id, message):
  """Send an email message.
  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.
  Returns:
    Sent Message.
  """
  try:
    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    print('Message Id: %s' % message['id'])
    return message
  except errors.HttpError as error:
    print('An error occurred: %s' % error)

def service_account_login():
  SCOPES = ['https://www.googleapis.com/auth/gmail.send']
  SERVICE_ACCOUNT_FILE = 'lisa_service_account.json'

  credentials = service_account.Credentials.from_service_account_file(
          SERVICE_ACCOUNT_FILE, scopes=SCOPES)
  delegated_credentials = credentials.with_subject(EMAIL_FROM)
  service = build('gmail', 'v1', credentials=delegated_credentials)
  return service


service = service_account_login()
# Call the Gmail API
#message = create_message(EMAIL_FROM, EMAIL_TO, EMAIL_SUBJECT, EMAIL_CONTENT)
#sent = send_message(service,'me', message)