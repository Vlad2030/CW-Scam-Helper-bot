import requests


def sendRequest(api):
    api_responce = requests.get(api)
    output = api_responce.text
    return output


result = sendRequest(api='')