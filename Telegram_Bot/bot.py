import requests
import json
import configparser as cfg
import profiles


class telegram_chatbot():
    
    #self.profile_dict = profiles.restart_points()
    
    def __init__(self, config):
        self.token = self.read_token_from_config_file(config)
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def get_updates(self, offset=None):
        url = self.base + "getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self, msg, chat_id):
        chat_id_2 = -459297051
        chat_url = self.base + "sendMessage?chat_id=" + str(chat_id_2) + "&text=" + msg
        
        url = self.base + "sendMessage?chat_id={}&text={}".format(chat_id, msg)
        
        ez420_id = -1001333125207
        ez420_url = self.base + "sendMessage?chat_id=" + str(ez420_id) + "&text=" + msg
        
        if msg is not None:
            #self dm
            #requests.get(url)
            
            #testing chat channel
            #requests.get(chat_url)
            
            #ez420 channel
            requests.get(ez420_url)
            
    def read_token_from_config_file(self, config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds', 'token')
    
    def random_picture(self, msg):
        return 'https://i.imgur.com/Qud9Obz.jpg'
    
    def send_photo(self, msg, chat_id):
        url = self.base + "sendPhoto?chat_id={}&text={}".format(chat_id, msg)
        if msg is not None:
            requests.get(url)
    
    #chooses what command to try to run
    def read_command(self, msg, name, profile_dict):
        #print(msg)
        if '!' == msg[0]:
            name = profiles.name_converter(name)
            if msg == '!points':
                msg = profiles.get_points(name, profile_dict[name])
            elif msg =='!all points':
                msg = profiles.get_all_points(profile_dict)
            elif msg =='!leaderboard':
                msg = profiles.get_leaderboard(profile_dict)
            else:
                print('Invalid Command')
                msg = '\nCOMMAND LIST:\n!points \n!all points \n!leaderboard'
            return msg
    