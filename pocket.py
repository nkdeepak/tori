
"""
    The main pocket class which performs all the fucntions related to getting data from pocket and also formatting

"""

from os.path import expanduser, isfile
import configparser


class Pocket():

    key = "88518-bab0e52844581f918ef5969d"
    config_file = expanduser('~/.kimo_pocket')
    config = configparser.ConfigParser(allow_no_value=True)
    token = ""

    def __init__(self):
        
        """Checking if the config file exists.
         If not recreate it with dummy values
        """
        if (not isfile(self.config_file)):
            self.config['kimo_pocket'] = {
                'code': '',
                'token': ''
            }
            with open(self.config_file, 'w') as configfile:
                self.config.write(configfile)
        """
            If the file exists read the OAUTH contents (code, token)
            If one of them are empty perform OAUTH again to get fresh token
        """
        self.config.read(self.config_file)
        code = self.config['kimo_pocket']['code']
        self.token = self.config['kimo_pocket']['token']

        code, token = self.get_oauth_details(code, self.token)

    def get_oauth_details(self, code, token):
        data = {
            'consumer_key': self.key,
            'redirect_url': 'https://criativo.ai'
        }

        if code=='' and token=='':
            pass            


        

    def get_list(self,tags):
        pass

    def format_item(self, item):
        pass