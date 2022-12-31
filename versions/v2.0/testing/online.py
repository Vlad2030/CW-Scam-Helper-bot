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

def SendRequest(Server, action, type=1):

    if type == 1:
        st = 'GET'

    if type == 2:
        st = "POST"

    curl = curl_unit()
    curl_setopt_array(curl, [
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
        ],
    ])

    responce = curl_exec(curl)
    err = curl_error(curl)
    curl_close(curl)

    if err:
        return False
    else:
        return responce
#http://gw-01.contractwarsgame.com/?action=load&expire=1671329774&sig=4b49ccebfe318c88fe6cde4951ab1911

FirstStep = SendRequest('http://gw-01.contractwarsgame.com/", "?action=init&platform=standalone&version=1.6797&email=avoca.cw%2B1%40gmail.com&password=1&savePass=False&passHashed=False')

if FirstStep == False:
    die('CURL Error')

print(f'FirstStep')

if FirstStep['data'] == true:
    print(
        f'''
            User HASH string: {}
            User result: {}
            User ss string: {}
            User message string: {}
            Server time: {}
            UserID: {}
        '''
    )












if($FirstStep === false) die ("CURL Error");
$FirstStep = json_decode($FirstStep, true);
echo print_r($FirstStep); echo "<br><br>";
if($FirstStep['data'] === true) {
    echo "User HASH string: ". ($FirstStep['hash']). "<br>";
    echo "User result: ". ($FirstStep['result']). "<br>";
    echo "User ss string: ". ($FirstStep['ss']). "<br>";
    echo "User message string: ". ($FirstStep['message']). "<br>";
    echo "Server time: ". ($FirstStep['time']). "<br>";
    echo "UserID: ". ($FirstStep['user_id']). "<br>";
    echo "Updated params: ". ($FirstStep['updated']). "<br>";
    echo "sessionHash params: ". ($FirstStep['sessionHash']). "<br><br><br>";
    
    $actions= "?action=load";
    $request_uri = $actions . "&expire=".(time()+3600);
    $data = base64_encode(utf8_encode("1.6797"));
    $SigHash = md5($FirstStep['ss']."".$request_uri."json=" . $data);
    

    
    
    
    echo "App HASH : ". ($SigHash). "<br>";
    echo "data : ". ($data). "<br>";
    echo "request_uri : ". ($request_uri). "<br>";
    echo "request with hash : ". ($request_uri."&sig=".$SigHash). "<br>";
    $SecondStep =  SendRequest("http://gw-01.contractwarsgame.com/", $request_uri."&sig=".$SigHash, 2);
    echo $SecondStep;
} else {
    die("First step ERROR: invalid data");
}
?>`












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