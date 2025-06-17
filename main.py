import requests
import datetime

# 텔레그램 봇 정보
BOT_TOKEN = "여기에_너의_봇_토큰"
CHAT_ID = "여기에_너의_chat_id"

# 오늘 날짜
today = datetime.datetime.now().strftime("%Y-%m-%d")

# 보낼 메시지
message = f"🚀 GPT 주식 알리미 테스트입니다.\n\n오늘은 {today}입니다.\n정상적으로 작동합니다."

# 텔레그램 전송
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": message
}

res = requests.post(url, data=payload)
print(res.status_code, res.text)
