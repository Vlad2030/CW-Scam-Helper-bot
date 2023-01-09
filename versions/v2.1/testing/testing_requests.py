import hashlib
import requests
import json
import time
import base64
from loguru import logger


class Login:
    def GetRequest(server, action, platform, version,
                   email, password, savePass, passHashed):
        try:
            result = (
                f"http://{server}/?action={action}" \
                f"&platform={platform}&version={version}" \
                f"&email={email}&password={password}" \
                f"&savePass={savePass}&passHashed={passHashed}" \
            )
            GET_request = requests.get(
                              result,
                              cookies={'PHPSESSID': '3453453445345'}
                          )
            GET_result = json.loads(GET_request.text)
        except Exception as excp:
            return logger.error("{excp}", excp=excp)
        finally:
            return GET_result


    def sendRequest(server, action, type):
        if type==1:
            request = requests.get(f'{server}{action}')
        elif type==2:
            request = requests.post(f'{server}{action}')
        else:
            logger.error('type error')
        try:
            response = json.loads(request.text)
        except Exception as excp:
            return logger.error("{excp}", excp=excp)
        finally:
            logger.success("{answer}", answer=response)
            return response


class Hash:
    @staticmethod
    def MD5Hash(text):
        try:
            hashed = hashlib.md5(text.encode("utf-8")).hexdigest()
        except Exception as excp:
            return logger.error("{excp}", excp=excp)
        finally:
            return hashed


get_test = Login.GetRequest(
               server="gw-01.contractwarsgame.com",
               action="init",
               platform="standalone",
               version="1.6797",
               email="online@yopmail.com",
               password="1",
               savePass="False",
               passHashed="False",
           )


"""
data = get_test['data']
hash = get_test['hash']
result = get_test['result']
ss = get_test['ss']
message = get_test['message']
time = get_test['time']
user_id = get_test['user_id']
updated = get_test['updated']
sessionHash = get_test['sessionHash']
"""


if get_test["data"]:
    actions = "?action=load"
    time_expire = int(time.time()) + 3600
    print(time_expire)
    request_uri = f"{actions}&expire={time_expire}"
    base64encoded_version = "MS42Nzk3"
    r_cookies = get_test.cookies
    SigHash = Hash.MD5Hash(
                  text=f'{get_test["ss"]}{request_uri}' \
                  f'json={base64encoded_version}'
              )
    result_post = f"http://gw-01.contractwarsgame.com/" \
                  f"{request_uri}&sig={SigHash}"
    print(result_post)
    get_post = requests.post(result_post)
    #hashed = json.load(get_post.text.read())
    hashed = get_post.text
    print(hashed)
else:
    logger.error("invalid data")
"""
{
    "data":true,
    "hash":"3f6dd18c2a6edb70b2a4bad9286563bf",
    "result":0,
    "ss":"ly8i2r8jug",
    "message":null,
    "time":"1672602799",
    "user_id":9808559,
    "updated":true,
    "sessionHash":""
}
"""
