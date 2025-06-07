import os
from linebot import LineBotApi
from linebot.models import TextSendMessage
from cat_logic import generate_message

LINE_CHANNEL_ACCESS_TOKEN = os.environ.get('LINE_CHANNEL_ACCESS_TOKEN')
YOUR_LINE_USER_ID = os.environ.get('YOUR_LINE_USER_ID')

def main():
    if not LINE_CHANNEL_ACCESS_TOKEN or not YOUR_LINE_USER_ID:
        print("錯誤：金鑰或 User ID 未設定！")
        return
    message = generate_message()
    print(f"準備發送訊息：\n{message}")
    try:
        line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
        line_bot_api.push_message(
            YOUR_LINE_USER_ID,
            TextSendMessage(text=message)
        )
        print("訊息發送成功！")
    except Exception as e:
        print(f"訊息發送失敗：{e}")

if __name__ == "__main__":
    main()
