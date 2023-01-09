def SendRequest(Server_=None, action_=None, type_=1, *_args_):
    
    
    if type_ == 1:
        st_ = "GET"
    # end if
    if type_ == 2:
        st_ = "POST"
    # end if
    curl_ = curl_init()
    curl_setopt_array(curl_, Array({CURLOPT_URL: Server_ + action_, CURLOPT_RETURNTRANSFER: True, CURLOPT_ENCODING: "", CURLOPT_MAXREDIRS: 10, CURLOPT_TIMEOUT: 30, CURLOPT_HTTP_VERSION: CURL_HTTP_VERSION_1_1, CURLOPT_CUSTOMREQUEST: st_, CURLOPT_POSTFIELDS: "", CURLOPT_HTTPHEADER: Array("Content-Type: application/json")}))
    response_ = curl_exec(curl_)
    err_ = curl_error(curl_)
    curl_close(curl_)
    if err_:
        return False
    else:
        return response_
    # end if
    
# end def SendRequest
label .http
#// gw-01.contractwarsgame.com/?action=load&expire=1671329774&sig=4b49ccebfe318c88fe6cde4951ab1911
FirstStep_ = SendRequest("http://gw-01.contractwarsgame.com/", "?action=init&platform=standalone&version=1.6797&email=avoca.cw%2B1%40gmail.com&password=1&savePass=False&passHashed=False")
if FirstStep_ == False:
    print("CURL Error")
    sys.exit()
# end if
FirstStep_ = php_json_decode(FirstStep_, True)
print(print_r(FirstStep_))
print("<br><br>")
if FirstStep_["data"] == True:
    print("User HASH string: " + FirstStep_["hash"] + "<br>")
    print("User result: " + FirstStep_["result"] + "<br>")
    print("User ss string: " + FirstStep_["ss"] + "<br>")
    print("User message string: " + FirstStep_["message"] + "<br>")
    print("Server time: " + FirstStep_["time"] + "<br>")
    print("UserID: " + FirstStep_["user_id"] + "<br>")
    print("Updated params: " + FirstStep_["updated"] + "<br>")
    print("sessionHash params: " + FirstStep_["sessionHash"] + "<br><br><br>")
    actions_ = "?action=load"
    request_uri_ = actions_ + "&expire=" + time() + 3600
    data_ = php_base64_encode(utf8_encode("1.6797"))
    SigHash_ = php_md5(FirstStep_["ss"] + "" + request_uri_ + "json=" + data_)
    print("App HASH : " + SigHash_ + "<br>")
    print("data : " + data_ + "<br>")
    print("request_uri : " + request_uri_ + "<br>")
    print("request with hash : " + request_uri_ + "&sig=" + SigHash_ + "<br>")
    SecondStep_ = SendRequest("http://gw-01.contractwarsgame.com/", request_uri_ + "&sig=" + SigHash_, 2)
    print(SecondStep_)
else:
    print("First step ERROR: invalid data")
    sys.exit()
# end if
