from linebot import LineBotApi, WebhookHandler

line_bot_api = LineBotApi('Kw13JfIApmcFO8ektLwB4vnvBpkKLxIYDnuqNA314zIzD9elCkDuQ3ABFDiGmMWrzZ6rKK393GaBR9l1ypcCcB3x0oD5ysZK9GhVysZrs550nZ834BJVvDTD9rzt+dp0kkXgv1J6bJQdo2ZkDD/gtQdB04t89/1O/w1cDnyilFU=')

with open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/Graph/Line Banner.jpg', 'rb') as f:
    line_bot_api.set_rich_menu_image('richmenu-52d999479e918ccbf0e59af8d8574efb', 'image/jpeg', f)