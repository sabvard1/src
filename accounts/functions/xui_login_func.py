import requests
from random import randint
from urllib.request import urlopen
import json

URL = 'http://test1.ss22ss.online:8443/'

URL_CONFIG = 'test1.ss22ss.online:'
LOGIN_ROUTE = 'login/'
INBOUNDS_LIST = "panel/api/inbounds/list"
ADD_CLIENT = "panel/api/inbounds/addClient"
CLIENT_DATA = "panel/api/inbounds/getClientTraffics/"
INBOUND_DATA = "panel/api/inbounds/get/"

cookies = {
    'lang': 'en-US',
    'session': 'MTcwNTk0OTkzOXxEdi1CQkFFQ180SUFBUkFCRUFBQWRmLUNBQUVHYzNSeWFXNW5EQXdBQ2t4UFIwbE9YMVZUUlZJWWVDMTFhUzlrWVhSaFltRnpaUzl0YjJSbGJDNVZjMlZ5XzRNREFRRUVWWE5sY2dIX2hBQUJCQUVDU1dRQkJBQUJDRlZ6WlhKdVlXMWxBUXdBQVFoUVlYTnpkMjl5WkFFTUFBRUxURzluYVc1VFpXTnlaWFFCREFBQUFCel9oQmtCQWdFSGMyRmlkbUZ5WkFFTFUyRmlaWEpBUURFek5qa0F8CKmu616B6aECbOl97SEPeC9obbZ5GnoJQ8VcLX5mJV0=',
}

s = requests.session()

login_payload = {
    'username' : 'sabvard',
    'password': 'Saber@@1369'
}



def get_email(email):
    print(email)


def login_request():
    login_req = s.post(URL + LOGIN_ROUTE, data=login_payload)

def add_client(email):
    random_number = randint(1000000,9999999)
    random_number1 = randint(100,999)
    setting_details = "{\"clients\":[{\"id\":\"95e4e7bb-7796-47e7-e8a7-f"+str(random_number)+"f"+str(random_number1)+"\",\"alterId\":0,\"email\":\""+email+"\",\"limitIp\":0,\"totalGB\":0,\"expiryTime\":0,\"enable\":true,\"tgId\":\"\",\"subId\":\"\"}]}"
    add_client_data = {
        "id": 1,
        "settings": setting_details

    }
    return requests.post(URL + ADD_CLIENT, data= add_client_data, cookies= cookies)
    

def get_clinet_data(email):
    return requests.get(URL + CLIENT_DATA + email, cookies= cookies)



def get_inbound_data(id_num, user_email):
    raw_data = requests.get(URL + INBOUND_DATA + id_num , cookies= cookies).json()
    
    str_to_json_settings = json.loads(raw_data["obj"]["settings"])
    
    str_to_json_streamSettings = json.loads(raw_data["obj"]["streamSettings"])
    
    def user_data_get():
        for i in str_to_json_settings["clients"]:
            if i["email"] == user_email:
                return i
                break
    user_data = user_data_get()
    
    user_id = user_data["id"]
    return {"raw_data": raw_data,
            "str_to_json_settings": str_to_json_settings,
            "str_to_json_streamSettings": str_to_json_streamSettings,
            "user_data": user_data,
            "user_id": user_id}


def config_gen(raw_data, user_id, str_to_json_streamSettings, user_email):
    return ((raw_data["obj"]["protocol"])+"://"+user_id+"@"+URL_CONFIG+str(raw_data["obj"]["port"])+"?type="+str_to_json_streamSettings["network"]+"&serviceName="+str_to_json_streamSettings['grpcSettings']['serviceName']+"&security="+str_to_json_streamSettings["security"]+"&pbk="+str_to_json_streamSettings["realitySettings"]["settings"]["publicKey"]+"&fp="+str_to_json_streamSettings["realitySettings"]["settings"]["fingerprint"]+"&sni="+str_to_json_streamSettings["realitySettings"]["serverNames"][0]+"&sid="+str_to_json_streamSettings["realitySettings"]["shortIds"][0]+"&spx=%2F#"+raw_data["obj"]["remark"]+"-"+user_email)












