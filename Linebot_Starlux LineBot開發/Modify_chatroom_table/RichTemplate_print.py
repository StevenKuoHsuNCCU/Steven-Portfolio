import requests

headers = {'Authorization':'Bearer Kw13JfIApmcFO8ektLwB4vnvBpkKLxIYDnuqNA314zIzD9elCkDuQ3ABFDiGmMWrzZ6rKK393GaBR9l1ypcCcB3x0oD5ysZK9GhVysZrs550nZ834BJVvDTD9rzt+dp0kkXgv1J6bJQdo2ZkDD/gtQdB04t89/1O/w1cDnyilFU='}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-52d999479e918ccbf0e59af8d8574efb', headers=headers)

print(req.text)