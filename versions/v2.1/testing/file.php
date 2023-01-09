<?php
	function sendRequest($Action)
    {
        $CurlInit = curl_init();
        curl_setopt_array($CurlInit, [
            CURLOPT_URL => requestServer.$Action,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_ENCODING => "",
            CURLOPT_MAXREDIRS => CURL_MaxRedirects,
            CURLOPT_TIMEOUT => CURL_Timeout,
            CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
            CURLOPT_CUSTOMREQUEST => "POST",
            CURLOPT_POSTFIELDS => "",
            CURLOPT_COOKIE => "PHPSESSID=".HashPHPSess,
            CURLOPT_HTTPHEADER => [
                "Content-Type: application/json",
            ]
        ]);
        $ServerResponse = curl_exec($CurlInit);
        $ServerError = curl_error($CurlInit);
        curl_close($CurlInit);
        if($ServerError)
        {
            return false;
        } else {
            return $ServerResponse;
        }
    }
    
    /*
        * SendRequestGzip
        * Version: 1.0.1
        * Description: 
    */
    function sendRequestGzip($Action)
    {
        $CurlInit = curl_init();
        curl_setopt_array($CurlInit, [
            CURLOPT_URL => requestServer.$Action,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_MAXREDIRS => CURL_MaxRedirects,
            CURLOPT_TIMEOUT => CURL_Timeout,
            CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
            CURLOPT_CUSTOMREQUEST => "POST",
            CURLOPT_POSTFIELDS => "",
            CURLOPT_COOKIE => "PHPSESSID=".HashPHPSess,
            CURLOPT_HTTPHEADER => [
                "Content-Type: application/x-www-form-urlencoded",
            ],
            CURLOPT_ENCODING => "gzip"
        ]);
        $ServerResponse = curl_exec($CurlInit);
        $ServerError = curl_error($CurlInit);
        curl_close($CurlInit);
        if($ServerError)
        {
            return false;
        } else {
            return $ServerResponse;
        }
    }
	function getOnline() 
    {
        $fAction = "?action=";
        $Action = "gethosts&type=with_friends&version=".clientVersion;
        $requestUri = $fAction.$Action.getSessionExpire();
        $userHashedSign = getBasicHash($initResponse['data']['ss'], $requestUri);
        $requestHostInfo = $requestUri."&sig=".$userHashedSign;
        $HostInfoRequest = sendRequest($requestHostInfo);
        if($HostInfoRequest === false) return false;
        $HostInfo = getDecodedZlib($HostInfoRequest);
        $playerCount = 0;
      $spectactorCount = 0;
    $loadPlayerCount = 0;
    $maxPlayers = 0;
    for($i = 0; $i < count($HostInfo['hosts']); $i++)
    {
      $playerCount += (int) $HostInfo['hosts'][$i]['playerCount'];
      $spectactorCount += (int) $HostInfo['hosts'][$i]['spectactorCount'];
      $loadPlayerCount += (int) $HostInfo['hosts'][$i]['loadPlayerCount'];
      $maxPlayers += (int) $HostInfo['hosts'][$i]['maxPlayers'];
    }
    $onlinePlayersCount = $playerCount + $spectactorCount + $loadPlayerCount;
    return "Online at ".date("d.m.Y h:i:s A", time())." is ".$onlinePlayersCount." (Playing: ".$playerCount."/".$maxPlayers.", Spectactors: ".$spectactorCount.", Loading Profile: ".$loadPlayerCount.")";
    }
	function getDecodedZlib($response) 
    {
        return json_decode(zlib_decode($response), true);
    }
?>