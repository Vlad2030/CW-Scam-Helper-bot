import requests
import json
import datetime
version = '1.6797'

def PlayerCount():
    return playercount + num

def SpectatorsCount():
    return spectatorscount + num2

def LoadPlayersCount():
    return loadplayerscount + num3

def MaxPlayers():
    return maxplayers + num4

def SendRequest():


    def Get(server, action):
        try:
            GET_request = requests.get(f'{server}{action}')
            return GET_request
        except:
            return print(f'Fail GET {server}:{action}:{GET_request}')    
    
    
    def Post(server, action):
        try:
            POST_request = requests.post(f'{server}{action}')
            return POST_request
        except:
            return print(f'Fail POST {server}:{action}:{POST_request}')

    while True:
        choice = input(
                    f'''
                        GET(1) or POST(2) or QUIT(q):
                    '''
                 )
        if choice == '1':
            FirstStep = Get(
                        'http://gw-01.contractwarsgame.com/',
                        '?action=init&platform=standalone&version=1.6797&email=avoca.cw%2B1%40gmail.com&password=1&savePass=False&passHashed=False'
                        )
        elif choice == '2':
            FirstStep = Post(
                        'http://gw-01.contractwarsgame.com/',
                        '?action=init&platform=standalone&version=1.6797&email=avoca.cw%2B1%40gmail.com&password=1&savePass=False&passHashed=False'
                        )
        elif choice == 'q':
            break
        else:
            print(f'Error, try again...')








def SendRequestTest(Server, action):
    if type == 1:
        st = 'GET'

    if type == 2:
        st = "POST"

    curl = curl_unit()
    curl_setopt_array(
        curl, [
            CURLOPT_URL => Server.action,
            CURLOPT_RETURNTRANSFER => True,
            CURLOPT_ENCODING => '',
            CURLOPT_MAXREDIRS => 10,
            CURLOPT_TIMEOUT => 30,
            CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
            CURLOPT_CUSTOMREQUEST => st,
            CURLOPT_POSTFIELDS => '',
            CURLOPT_HTTPHEADER => [
                'Content-Type: application/json'
            ]
        ]
    )

    responce = curl_exec(curl)
    err = curl_error(curl)
    curl_close(curl)

    if err:
        return False
    else:
        return responce

#http://gw-01.contractwarsgame.com/?action=load&expire=1671329774&sig=4b49ccebfe318c88fe6cde4951ab1911

FirstStep = SendRequest(
    'http://gw-01.contractwarsgame.com/',
    '?action=init&platform=standalone&version=1.6797&email=avoca.cw%2B1%40gmail.com&password=1&savePass=False&passHashed=False'
)

if FirstStep == False:
    die('CURL Error')

print(f'FirstStep')

if FirstStep['data'] == true:
    print(
        f'''
            User HASH string: {FirstStep['hash']}\n
            User result: {FirstStep['result']}\n
            User ss string: {FirstStep['ss']}\n
            User message string: {FirstStep['message']}\n
            Server time: {FirstStep['time']}\n
            UserID: {FirstStep['user_id']}\n
            Updated params: {FirstStep['updated']}\n
            sessionHash params: {FirstStep['sessionHash']}\n
        '''
    )
    actions = '?action=load'
    time_now = timedate.timedate.now()
    request_uri = f'{actions}&expire={time_now}'
    data = base64_encode(utf8_encode("1.6797"))
    SigHash = md5('{FirstStep['ss']}{request_uri}json={data}'
    print(
        f'''
            App HASH: {SigHash}\n
            data: {data}\n
            request_uri: {request_uri}\n
            request with hash: {request_uri}&sig={SigHash}\n
        '''
    )
    SecondStep = SendRequest(
        'http://gw-01.contractwarsgame.com/',
        f'{request_uri}&sig={SigHash}',
        2
    )
    print(SecondStep)
else:
    die('First step Error: invalid data')























def Online():
    global num, num2, num3, num4
    num = 0
    num2 = 0
    num3 = 0
    num4 = 0

    num += 
    num3 +=
    num4 +=
    num2 +=

    num5 = num + num3 + num4
    time_now = datetime.datetime.now(
        %c
    )
    print(
        f'online at {time_now} is {num5} (Playing: {num}/{num2} Spectators: {num3}, Loading Profile: {num4})')

Online()