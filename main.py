from flask import Flask, request, abort

from linebot.v3 import (
    WebhookHandler,
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)

from azure_openai import ask_azure_gpt

import os


app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return "LINE Chatbot Webhook is running!"

configuration = Configuration(access_token=os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        answer = ask_azure_gpt(event.message.text)
        if (answer is None):
            answer = "Sorry, I don't understand"

        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=answer)]
            )
        )

@app.route("/webhook", methods=['POST'])
def webhook():

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

    return "OK"

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    debug = bool(os.environ.get("DEBUG", False))

    app.run("0.0.0.0", port=int(port), debug=debug)
