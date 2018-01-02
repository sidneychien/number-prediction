import json
import urllib, urllib2
import base64

serverURL = "http://vop.baidu.com/server_api"
token = ""
testFileName = ""
apiKey  = "youkey"
secretKey = "youkey"
cuid = "C9-9C-DC-EF-03-30"

def getToken():
    getTokenURL = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials" + "&client_id=" + apiKey + "&client_secret=" + secretKey
    response = json.loads(urllib.urlopen(getTokenURL).read())
    #print response
    return response['access_token']

def getResult():
    token = getToken()

    speech_file = 'tts_test.wav'
    #speech_file = 'weixin.wav'
    with open(speech_file, 'rb') as f:
        speech_data = f.read()
        speech_base64=base64.b64encode(speech_data).decode('utf-8')
    speech_length=len(speech_data)
    params = {
        'format':'pcm',
        'rate':16000,
        'channel':'1',
        'token':token,
        'cuid':cuid,
        'lan':'zh',
        'len':speech_length,
        'speech':speech_base64
    }
    json_data = json.dumps(params).encode('utf-8')
    json_length = len(json_data)
    request = urllib2.Request(url=serverURL)
    request.add_header("Content-Type", "application/json")
    request.add_header("Content-Length", json_length)
    fs = urllib2.urlopen(url=request, data=json_data)

    result_str = fs.read().decode('utf-8')
    json_resp = json.loads(result_str)
    res = json.dumps(json_resp,ensure_ascii=False)
    return  res



