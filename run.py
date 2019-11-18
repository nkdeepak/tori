from pocket_bak import AuthHandler, PocketHandler
import gmail
from intro_mail_txt import msg_txt


verbose = False
direct = False
auth = AuthHandler(verbose)
pocket = PocketHandler(auth, verbose, direct)
EMAIL_FROM = 'lisa@criativo.ai'
user_details = [
    {
        'name': 'Rens',
        'email': 'rens@kimo.ai'
    },
    {
        'name': 'Obrian',
        'email': 'obrian@kimo.ai'
    },
    {
        'name': "Krishna",
        'email': "krishna@kimo.ai"
    }
]

tmp_details = [
    {
        'name': 'Krishna',
        'email': 'deepak.nallamilli@gmail.com'
    },
    {
        'name': 'Deepak',
        'email': 'deepaknk@aditya.ac.in'
    }
]
EMAIL_SUBJECT = 'Hello  from LISA !'

def fetch_data(tag):
    return pocket.list_filtered(tag)

def format_data(tag, u_name):
    data=[]
    json = fetch_data(tag)
    for item in sorted(json.values(), key=lambda item: item['sort_id']):
            try:
                title = item['resolved_title']
            except KeyError:
                title = '<no title found>'
            if direct:
                msg = "{}: {}"
                print(msg.format(title, item['given_url']))
            else:
                link = "https://app.getpocket.com/read/{}"
                tmp_dict = {}
                tmp_dict['title'] = title
                tmp_dict['link'] = link.format(item['item_id'])
                data.append(tmp_dict)
                #print(msg.format(title, item['item_id']))
    
    final_txt = msg_txt.format(data[0]['title'], data[0]['link'], data[1]['title'], data[1]['link'], data[2]['title'], data[2]['link'], name=u_name)
    return final_txt


def send_mail(key):
    if key == 'test':
        details = tmp_details
    else:
        details = user_details
    service = gmail.service_account_login()
    for user in details:
        user_name = user['name']
        user_email = user['email']
        msg_txt = format_data("kimoshare", user_name)
        
        message = gmail.create_message(EMAIL_FROM, user_email, EMAIL_SUBJECT, msg_txt)
        gmail.send_message(service, 'me', message)

    return True

        
    

def run(tag):
    pass



if __name__ == "__main__":
    key = 'share'
    #msg_txt = format_data("kimoshare")
    if(send_mail(key)):
        print ("Success")
    else:
        print ("Fail")
    
    