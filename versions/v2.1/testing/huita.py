import hashlib
import requests
import json
import time
import base64
from loguru import logger


class Login:
    @staticmethod
    def GetRequest(
        server, action, platform, version, email, password, savePass, passHashed
    ):
        try:
            result = (
                f"http://{server}/?action={action}"
                f"&platform={platform}&version={version}"
                f"&email={email}&password={password}"
                f"&savePass={savePass}&passHashed={passHashed}"
            )
            GET_request = requests.get(result)
            GET_result = json.loads(GET_request.text)
        except Exception as excp:
            return logger.error("{excp}", excp=excp)
        finally:
            logger.success("{answer}", answer=GET_request)
            return GET_result

    def PostRequest(
        server, action, platform, version, email, password, savePass, passHashed
    ):
        try:
            result = (
                f"http://{server}/?action={action}"
                f"&platform={platform}&version={version}"
                f"&email={email}&password={password}"
                f"&savePass={savePass}&passHashed={passHashed}"
            )
            POST_request = requests.post(result)
            POST_result = json.loads(POST_request.text)
        except Exception as excp:
            return logger.error("{excp}", excp=excp)
        finally:
            return POST_result


class Hash:
    @staticmethod
    def md5(text):
        if isinstance(text, bool):
            if text == True:
                text = "1"
            else:
                text = "0"
        elif isinstance(text, int):
            text = str(text)
        elif isinstance(text, int):
            text = str(text)
        if isinstance(text, type(str)):
            # Only work when given text is string
            return hashlib.md5(text.encode("utf-8")).hexdigest()

        # When text not str type
        return ""

    def MD5Hash(GET_result):
        try:

            return
        except Exception as excp:
            return logger.error("{excp}", excp=excp)
        finally:
            return


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
    request_uri = f"{actions}&expire={time_expire}"
    data = str(
        base64.b64encode(str("1.6797".encode("utf-8"), "utf-8").encode("utf-8")),
        "utf-8",
    )
    SigHash = Settlement.md5(
        str(str(str(str(FirstStep["ss"]) + "") + str(request_uri)) + "json=")
        + str(data)
    )
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
