import requests
import json
# 設定 headers，輸入你的 Access Token，記得前方要加上「Bearer 」( 有一個空白 )
headers = {'Authorization':'Bearer Kw13JfIApmcFO8ektLwB4vnvBpkKLxIYDnuqNA314zIzD9elCkDuQ3ABFDiGmMWrzZ6rKK393GaBR9l1ypcCcB3x0oD5ysZK9GhVysZrs550nZ834BJVvDTD9rzt+dp0kkXgv1J6bJQdo2ZkDD/gtQdB04t89/1O/w1cDnyilFU=','Content-Type':'application/json'}

body = {
    'size': {'width': 800, 'height': 540},   # 設定尺寸
    'selected': 'true',                        # 預設是否顯示
    'name': 'Richmenu demo',                   # 選單名稱
    'chatBarText': '查看更多資訊',            # 選單在 LINE 顯示的標題 ####很重要
    'areas':[                                  # 選單內容
        {
          'bounds': {'x': 0, 'y': 270, 'width': 266, 'height': 270}, # 選單位置與大小
          'action': {'type': 'uri', 'uri': 'https://shop.jx-starlux.com'}                # 點擊後傳送文字
        },
        {
          'bounds': {'x': 266, 'y': 270, 'width': 267, 'height': 270},
          'action': {'type': 'postback', 'data': 'schedule'}
        },
        {
          'bounds': {'x': 533, 'y': 270, 'width':267, 'height': 270},
          'action': {'type': 'postback', 'data': 'mileage'}
        },
        {
          'bounds': {'x': 0, 'y': 0, 'width': 800, 'height': 270},
          'action': {'type': 'postback', 'data': 'popup'}
        }
    ]
  }

# 向指定網址發送 request
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
                      headers=headers,data=json.dumps(body).encode('utf-8'))
# 印出得到的結果
print(req.text)
