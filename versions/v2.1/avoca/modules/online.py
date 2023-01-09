import requests

api='http://avoca.beget.tech/'

def sendRequest():
    api_responce = requests.get(api)
    output = api_responce.text
    return output
