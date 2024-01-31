from flask import Flask, request, abort
import json
import requests
from linebot import ( LineBotApi, WebhookHandler )
from linebot.exceptions import ( InvalidSignatureError )
from linebot.models import ( MessageEvent, BubbleContainer, ImageComponent, FlexSendMessage, TextMessage, TextSendMessage, PostbackEvent, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, ConfirmTemplate, PostbackAction, MessageAction, RichMenu, RichMenuSize, RichMenuArea, RichMenuBounds, URIAction, CarouselTemplate, CarouselColumn, LocationAction, LocationMessage, QuickReply, QuickReplyButton, DatetimePickerAction)


import pandas as pd


"""************************************** LineBot Default **********************************************************************************************"""


app = Flask(__name__)

line_bot_api = LineBotApi('Kw13JfIApmcFO8ektLwB4vnvBpkKLxIYDnuqNA314zIzD9elCkDuQ3ABFDiGmMWrzZ6rKK393GaBR9l1ypcCcB3x0oD5ysZK9GhVysZrs550nZ834BJVvDTD9rzt+dp0kkXgv1J6bJQdo2ZkDD/gtQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0bb894c75b168a8f86aa286830cba87a')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


"""************************************** LineBot Data **********************************************************************************************"""
# User Data
traveler_name = ["鍾雨彤","王韻婷","王冠媛","張瀚宇","溫郁佳","許慈倩","蔡甄芳","陳冠瑩","李蕙妤","黃宇秀","林禹彤"]
traveler_userID = list()

adventurer_name = ["藍雅馨","陳芳榆","莊芷芸","陳昱宏","廖立人","莊雃涵","蔡佩妤","陳子萱","陳佳瑜","鄭雅薰","莊子嫻","曾雅萍","劉奕伶","張祐榮","黃品豪"]
adventurer_userID = list()

explorer_name = ["盛鈺庭","劉芷沅","連姵瑜","羅莠茹","蔡甄芳","黃芷葳","粱怡玟","邱品蓉","廖于瑄","陳亭妤","張淨淇","郭泳沛","陳芳琦","成欣","陳佳儀"]
explorer_userID = list()

insighter_name = ["郭許謙","郭許明","洪翊婕","葉瀚元","周宗在","陳思濡","楊宥群","張杰洋","廖立人","黃廷雅","李姁蓁","吳宛樺","王緁萱","陳凱柔","俞懷媃","吳文傑","邱郁文","白佩玉","費喬登"]
insighter_userID = list()

All_user_ID = list()



"""************************************** Data Analysis **********************************************************************************************"""

## explorer, insighter sale begin  sale_1 == 1
sale_1 = 0
## traveler, adventurer sale begin  sale_2 ==1
sale_2 = 0


# Quick Save Text Message
QSTM = dict()        #QSTM["mes{0}".format(event.source.user_id)]


# Browsing History
BH = dict()          #BH["bh{0}".format(event.source.user_id)]

# Gender Selection
GS = dict()          #GS["gs{0}".format(event.source.user_id)]

# people who finished questionnaire
FQ = list()



"""************************************** Function **********************************************************************************************"""


def MembershipLogin(UserName):
    if UserName in traveler_name:
        return "traveler"
    elif UserName in adventurer_name:
        return "adventurer"
    elif UserName in explorer_name:
        return "explorer"
    elif UserName in insighter_name:
        return "insighter"


def MembershipIdentification(UserID):
    if UserID in traveler_userID:
        return "traveler"
    elif UserID in adventurer_userID:
        return "adventurer"
    elif UserID in explorer_userID:
        return "explorer"
    elif UserID in insighter_userID:
        return "insighter"
    else:
        return "error"
        
    









"""************************************** LineBot Reaction **********************************************************************************************"""



@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    ## claim the global
    global sale_1
    global sale_2
    global QSTM
    global GS
    global BH
    global All_user_ID
    global traveler_name
    global traveler_userID
    global adventurer_name
    global adventurer_userID
    global explorer_userID
    global explorer_name
    global insighter_name
    global insighter_userID
    global FQ
    

    
    ## clean the previous message
    if "mes{0}".format(event.source.user_id) in QSTM:
         del QSTM["mes{0}".format(event.source.user_id)]
   
    
    ##Collect all user_id
    if str(event.source.user_id) not in All_user_ID:
        All_user_ID.append(str(event.source.user_id))
        BH["bh{0}".format(event.source.user_id)] = "danang"
        GS["gs{0}".format(event.source.user_id)] = "female"
    print(All_user_ID)
    
    
    # Save user message 
    QSTM["mes{0}".format(event.source.user_id)] = str(event.message.text)
    
    
    
    
    if str(event.message.text) == "k":
        print(All_user_ID,4,insighter_userID,6)
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/test.json', 'r', encoding='utf-8'))
            ))
    elif str(event.message.text) == "sale1":
         sale_1 = 1
         for i in All_user_ID:
            if BH["bh{0}".format(i)] == "tokyo":
                line_bot_api.push_message( i , FlexSendMessage(alt_text="請選擇以下服務",
                    contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/tokyo_trip.json', 'r', encoding='utf-8'))
                ))
            elif BH["bh{0}".format(i)] == "fukuoka":
                line_bot_api.push_message( i , FlexSendMessage(alt_text="請選擇以下服務",
                    contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/fukuoka_trip.json', 'r', encoding='utf-8'))
                ))
            elif BH["bh{0}".format(i)] == "osaka":
                line_bot_api.push_message( i , FlexSendMessage(alt_text="請選擇以下服務",
                    contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/tokyo_trip.json', 'r', encoding='utf-8'))
                ))
            elif BH["bh{0}".format(i)] == "okinawa":
                line_bot_api.push_message( i , FlexSendMessage(alt_text="請選擇以下服務",
                    contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/cebu_trip.json', 'r', encoding='utf-8'))
                ))
            elif BH["bh{0}".format(i)] == "sapporo":
                line_bot_api.push_message( i , FlexSendMessage(alt_text="請選擇以下服務",
                    contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/sapporo_trip.json', 'r', encoding='utf-8'))
                ))
                # Phillipines
            elif BH["bh{0}".format(i)] == "cebu":
                line_bot_api.push_message( i , FlexSendMessage(alt_text="請選擇以下服務",
                    contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/cebu_trip.json', 'r', encoding='utf-8'))
                ))
            elif BH["bh{0}".format(i)] == "manila":
                line_bot_api.push_message( i , FlexSendMessage(alt_text="請選擇以下服務",
                    contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/cebu_trip.json', 'r', encoding='utf-8'))
                ))
                # Macau
            elif BH["bh{0}".format(i)] == "macau":
                line_bot_api.push_message( i , FlexSendMessage(alt_text="請選擇以下服務",
                    contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/macau_trip.json', 'r', encoding='utf-8'))
                ))
                # Thailand
            elif BH["bh{0}".format(i)] == "bangkok":
                line_bot_api.push_message( i , FlexSendMessage(alt_text="請選擇以下服務",
                    contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/bangkok_trip.json', 'r', encoding='utf-8'))
                ))
                # Singapore
            elif BH["bh{0}".format(i)] == "singapore":
                line_bot_api.push_message( i , FlexSendMessage(alt_text="請選擇以下服務",
                    contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/singapore_trip.json', 'r', encoding='utf-8'))
                ))
                # Malaysia
            elif BH["bh{0}".format(i)] == "kuala":
                line_bot_api.push_message( i , FlexSendMessage(alt_text="請選擇以下服務",
                    contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/cebu_trip.json', 'r', encoding='utf-8'))
                ))
            elif BH["bh{0}".format(i)] == "penang":
                line_bot_api.push_message( i , FlexSendMessage(alt_text="請選擇以下服務",
                    contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/singapore_trip.json', 'r', encoding='utf-8'))
                ))
                # Vietnam
            elif BH["bh{0}".format(i)] == "danang":
                line_bot_api.push_message( i , FlexSendMessage(alt_text="請選擇以下服務",
                    contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/danang_trip.json', 'r', encoding='utf-8'))
                ))
            elif BH["bh{0}".format(i)] == "hochiminh":
                line_bot_api.push_message( i , FlexSendMessage(alt_text="請選擇以下服務",
                    contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/hochiminh_trip.json', 'r', encoding='utf-8'))
                ))
            
                
         
    
         # Push vip trip
    elif str(event.message.text) == "vip":
        for i in insighter_userID :
            print(i)
            line_bot_api.push_message( i , FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/sapporo_trip_vip.json', 'r', encoding='utf-8'))
             ))
        for i in explorer_userID :
            print(i)
            line_bot_api.push_message( i , FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/sapporo_trip_vip.json', 'r', encoding='utf-8'))
             ))
        
         # Push new product
    elif str(event.message.text) == "new product":
        for i in All_user_ID:
            if GS["gs{0}".format(i)] == "male":
                line_bot_api.push_message( i , FlexSendMessage(alt_text="請選擇以下服務",
                    contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/new_product_male.json', 'r', encoding='utf-8'))
                ))
            else:
                line_bot_api.push_message( i , FlexSendMessage(alt_text="請選擇以下服務",
                    contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/new_product_female.json', 'r', encoding='utf-8'))
                ))
            
    else:
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/TextSendMessage.json', 'r', encoding='utf-8'))
            ))

         
   
    
    
    
    
    
    
    
    
        

  


@handler.add(PostbackEvent)
def handle_message(event):
    
    ## claim the global
    global sale_1
    global sale_2
    global QSTM
    global GS
    global BH
    global All_user_ID
    global traveler_name
    global traveler_userID
    global adventurer_name
    global adventurer_userID
    global explorer_userID
    global explorer_name
    global insighter_name
    global insighter_userID
    global FQ
   
    
    
    #Collect all user_id
    if str(event.source.user_id) not in All_user_ID:
        BH["bh{0}".format(event.source.user_id)] = "danang"
        GS["gs{0}".format(event.source.user_id)] = "female"
        All_user_ID.append(str(event.source.user_id))
    print(All_user_ID)
    
    #Text Send Message
    
    ## membership login
    if str(event.postback.data) == "membership":
        if  QSTM["mes{0}".format(event.source.user_id)] in traveler_name:
            traveler_userID.append(str(event.source.user_id))
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text= "{0} 貴賓您好😊，您的會員級別為  🚩Traveler 旅行者。 您可以在圖文選單上點選『累積里程』 查看您的會員卡、里程資訊。".format(QSTM["mes{0}".format(event.source.user_id)])
                ))
        elif QSTM["mes{0}".format(event.source.user_id)] in adventurer_name:
            adventurer_userID.append(str(event.source.user_id))
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text= "{0} 貴賓您好😊，您的會員級別為  🚩Adventurer 冒險者。 您可以在圖文選單上點選『累積里程』 查看您的會員卡、里程資訊。".format(QSTM["mes{0}".format(event.source.user_id)])
                ))
        elif QSTM["mes{0}".format(event.source.user_id)] in explorer_name:
            explorer_userID.append(str(event.source.user_id))
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text= "{0} 貴賓您好😊，您的會員級別為  🚩Explorer 探險者。 您可以在圖文選單上點選『累積里程』 查看您的會員卡、里程資訊。".format(QSTM["mes{0}".format(event.source.user_id)])
                ))
        elif QSTM["mes{0}".format(event.source.user_id)] in insighter_name:
            insighter_userID.append(str(event.source.user_id))
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text= "{0} 貴賓您好😊，您的會員級別為  🚩Insighter 前瞻者。 您可以在圖文選單上點選『累積里程』 查看您的會員卡、里程資訊。".format(QSTM["mes{0}".format(event.source.user_id)])
                ))
        else:
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text= "{0}貴賓您好😊，您尚未加入星宇航空 Cosmile會員，您可以透過星宇航空官網進行註冊。{1}".format(QSTM["mes{0}".format(event.source.user_id)],"https://www.starlux-airlines.com/zh-TW/cosmile/cosmile")
                ))
            
    ##Clean the text message
    if "mes{0}".format(event.source.user_id) in QSTM:
         del QSTM["mes{0}".format(event.source.user_id)]
        
        
    ## Greeting
    if str(event.postback.data) == "Greeting":
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/Greeting.json', 'r', encoding='utf-8'))
            ))   
        
    ## Customer Service
    if str(event.postback.data) == "customer_service":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text= "貴賓您好，我們已收到您的反應，客服專員將會在一個工作日內回覆您，請您耐心等候🙂。謝謝您～")
                )
    

    
    # Schedule
    
    if str(event.postback.data) == "schedule":
         line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/schedule.json', 'r', encoding='utf-8'))
            ))
    if str(event.postback.data) == "schedule_japan":
         line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/schedule_japan.json', 'r', encoding='utf-8'))
            ))
    if str(event.postback.data) == "schedule_phillipines":
         line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/schedule_phillipines.json', 'r', encoding='utf-8'))
            ))
    if str(event.postback.data) == "schedule_thailand":
         line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/schedule_thailand.json', 'r', encoding='utf-8'))
            ))
    if str(event.postback.data) == "schedule_vietnam":
         line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/schedule_vietnam.json', 'r', encoding='utf-8'))
            ))
    if str(event.postback.data) == "schedule_malaysia":
         line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/schedule_malaysia.json', 'r', encoding='utf-8'))
            ))
    if str(event.postback.data) == "schedule_macau":
         line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/schedule_macau.json', 'r', encoding='utf-8'))
            ))
    if str(event.postback.data) == "schedule_singapore":
         line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/schedule_singapore.json', 'r', encoding='utf-8'))
            ))
         
    # packages
    if str(event.postback.data) == "schedule_japan_tokyo_hotel":
         line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="目前所有城市都尚未有套裝行程，我們即將推出，敬請期待😉"))
         BH["bh{0}".format(event.source.user_id)] = "tokyo"
    if str(event.postback.data) == "schedule_japan_osaka_hotel":
         line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="目前所有城市都尚未有套裝行程，我們即將推出，敬請期待😉"))
         BH["bh{0}".format(event.source.user_id)] = "osaka"
    if str(event.postback.data) == "schedule_japan_fukuoka_hotel":
         line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="目前所有城市都尚未有套裝行程，我們即將推出，敬請期待😉"))
         BH["bh{0}".format(event.source.user_id)] = "fukuoka"
    if str(event.postback.data) == "schedule_japan_okinawa_hotel":
         line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="目前所有城市都尚未有套裝行程，我們即將推出，敬請期待😉"))
         BH["bh{0}".format(event.source.user_id)] = "okinawa"
    if str(event.postback.data) == "schedule_japan_sapporo_hotel":
         line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="目前所有城市都尚未有套裝行程，我們即將推出，敬請期待😉"))
         BH["bh{0}".format(event.source.user_id)] = "sapporo"
    if str(event.postback.data) == "schedule_macau_macau_hotel":
         line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="目前所有城市都尚未有套裝行程，我們即將推出，敬請期待😉"))
         BH["bh{0}".format(event.source.user_id)] = "macau"
    if str(event.postback.data) == "schedule_singapore_singapore_hotel":
         line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="目前所有城市都尚未有套裝行程，我們即將推出，敬請期待😉"))
         BH["bh{0}".format(event.source.user_id)] = "singapore"
    if str(event.postback.data) == "schedule_thailand_bangkok_hotel":
         line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="目前所有城市都尚未有套裝行程，我們即將推出，敬請期待😉"))
         BH["bh{0}".format(event.source.user_id)] = "bangkok"
    if str(event.postback.data) == "schedule_malaysia_kuala_hotel":
         line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="目前所有城市都尚未有套裝行程，我們即將推出，敬請期待😉"))
         BH["bh{0}".format(event.source.user_id)] = "kuala"
    if str(event.postback.data) == "schedule_malaysia_penang_hotel":
         line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="目前所有城市都尚未有套裝行程，我們即將推出，敬請期待😉"))
         BH["bh{0}".format(event.source.user_id)] = "penang"
    if str(event.postback.data) == "schedule_vietnam_hochiminh_hotel":
         line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="目前所有城市都尚未有套裝行程，我們即將推出，敬請期待😉"))
         BH["bh{0}".format(event.source.user_id)] = "hochiminh"
    if str(event.postback.data) == "schedule_vietnam_danang_hotel":
         line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="目前所有城市都尚未有套裝行程，我們即將推出，敬請期待😉"))
         BH["bh{0}".format(event.source.user_id)] = "danang"
    if str(event.postback.data) == "schedule_phillipines_cebu_hotel":
         line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="目前所有城市都尚未有套裝行程，我們即將推出，敬請期待😉"))
         BH["bh{0}".format(event.source.user_id)] = "cebu"
    if str(event.postback.data) == "schedule_phillipines_manila_hotel":
         line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="目前所有城市都尚未有套裝行程，我們即將推出，敬請期待😉"))
         BH["bh{0}".format(event.source.user_id)] = "manila"

    
    #pop up store
    
    if str(event.postback.data) == "popup":
         line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/popup.json', 'r', encoding='utf-8'))
            ))
    if str(event.postback.data) == "draw":
         line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/questionnaire_gender.json', 'r', encoding='utf-8'))
            ))
    if str(event.postback.data) == "male":
         line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/questionnaire_age.json', 'r', encoding='utf-8'))
            ))
         GS["gs{0}".format(event.source.user_id)] = "male"
    if str(event.postback.data) == "female":
         line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/questionnaire_age.json', 'r', encoding='utf-8'))
            ))
         GS["gs{0}".format(event.source.user_id)] = "female"
    if str(event.postback.data) == "20_30":
         line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/questionnaire_travel.json', 'r', encoding='utf-8'))
            ))
    if str(event.postback.data) == "30_40":
         line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/questionnaire_travel.json', 'r', encoding='utf-8'))
            ))
    if str(event.postback.data) == "40_50":
         line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/questionnaire_travel.json', 'r', encoding='utf-8'))
            ))
    if str(event.postback.data) == "food":
         FQ.append(str(event.source.user_id))
         line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="問卷填答完畢，感謝您的耐心🙂，您可以至『我的抽獎卷』查看您的抽獎資格。"))
    if str(event.postback.data) == "scene":
         FQ.append(str(event.source.user_id))
         line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="問卷填答完畢，感謝您的耐心🙂，您可以至『我的抽獎卷』查看您的抽獎資格。"))
    if str(event.postback.data) == "shopping":
         FQ.append(str(event.source.user_id))
         line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="問卷填答完畢，感謝您的耐心🙂，您可以至『我的抽獎卷』查看您的抽獎資格。"))
    if str(event.postback.data) == "flight":
         FQ.append(str(event.source.user_id))
         line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="問卷填答完畢，感謝您的耐心🙂，您可以至『我的抽獎卷』查看您的抽獎資格。"))
         
    ## my ticket
    if str(event.postback.data) == "ticket":
         if str(event.source.user_id) in FQ:
             line_bot_api.reply_message(
             event.reply_token,
             FlexSendMessage(alt_text="請選擇以下服務",
             contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/ticket.json', 'r', encoding='utf-8'))
             ))
         else:
             line_bot_api.reply_message(
             event.reply_token,
             TextSendMessage(text="您尚未擁有抽獎券，您可以透過『點我填問卷抽機票』獲得抽獎機會🙂。"))
         
             
         
    
    ## new product
    if str(event.postback.data) == "new_product":
         line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/new_product_female.json', 'r', encoding='utf-8'))
            ))
    
    
    
    
         
    #mileage
         
    if str(event.postback.data) == "mileage":
        ## membership indentification
        membership = MembershipIdentification(str(event.source.user_id))
        if membership == "error":
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="請在聊天室輸入您的中文姓名，我們會為您確認會員等級。"))
               
        
        if membership == "traveler":
            line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/traveler.json', 'r', encoding='utf-8'))
            ))
        if membership == "adventurer":
            line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/adventurer.json', 'r', encoding='utf-8'))
            ))
        if membership == "explorer":
            line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/explorer.json', 'r', encoding='utf-8'))
            ))
        if membership == "insighter":
            line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="請選擇以下服務",
                contents = json.load(open('/Users/stevenkuo/College Course/大二/行銷管理/Starlux linebot/insighter.json', 'r', encoding='utf-8'))
            ))
            
            
    

         
         
         

if __name__ == "__main__":
    app.run(debug=True,port=6060)