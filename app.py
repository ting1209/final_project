from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('Msc/IbeSbasFg0g/D1FHUFnH8okZth5pisE52zaIv1G6f2zoWc4xn8qQgiY7YT7/JVI2ClQ/G2NYd40AMKtP/V0VHUHbEQVRLjr1G/e2PY+TP4rcTGohXvsIWmPWwFQD82EitDN/8dDZLBq6slrJ/AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('fceab7fd8c077ba66c52a881c32d7948')

# 監聽所有來自 /callback 的 Post Request
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
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

