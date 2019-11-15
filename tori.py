


class AuthHandler:
    key = '11411-11f6716adafdbf8ee3401509'
    rc_file = expanduser('~/.pocketrc')
    config = configparser.ConfigParser(allow_no_value=True)
    token = ""

    def __init__(self, verbose):
        self.verbose = verbose
        # load config, perform oauth if necessary
        if (not isfile(self.rc_file)):
            print("Config file not found, recreating.")
            self.config['OAUTH'] = {
                'code': '',
                'token': ''
            }
            with open(self.rc_file, 'w') as configfile:
                self.config.write(configfile)

        self.config.read(self.rc_file)
        code = self.config['OAUTH']['code']
        self.token = self.config['OAUTH']['token']
        if (self.token == '' and code == ''):
            # no token, no code, start oauth
            code = self.oauth_code(self.key)
            self.config['OAUTH']['code'] = code
            with open(self.rc_file, 'w') as configfile:
                self.config.write(configfile)
            exit()
        elif (self.token == ''):
            # got code, get token
            self.token = self.oauth_token(self.key, code)
            self.config['OAUTH']['token'] = self.token
            with open(self.rc_file, 'w') as configfile:
                self.config.write(configfile)
            # else: everything shiny
    # oauth

    def oauth_code(self, key):
        values = {
            'consumer_key': key,
            'redirect_uri': 'https://getpocket.com/connected_accounts'
        }

        response = self.request(values, request_url)
        code = response['code']
        message = ("Please open "
                   "https://getpocket.com/auth/authorize?request_token={0}"
                   "&redirect_uri=https://getpocket.com/connected_accounts"
                   " in your browser, authorize pocket-cli and run pocket-cli again.")
        print(message.format(code))
        return code

    def oauth_token(self, key, reqcode):
        values = {
            'consumer_key': key,
            'code': reqcode
        }

        resp_objects = self.request(values, authorize_url)
        # print(resp_objects)
        token = resp_objects['access_token']
        return token

    def request(self, values, target_url):
        data = urlencode(values)
        data = data.encode('UTF-8')
        req = Request(target_url, data)
        response = urlopen(req)
        # error handling
        if (response.status != 200):
            raise Exception(
                "Expected code 200, got {}".format(response.status))
        # replace with parse_qs?
        return dict(parse_qsl(response.read().decode('UTF-8')))