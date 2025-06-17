import requests
import datetime

# 텔레그램 봇 정보
TOKEN = "7805897776:AAG-c4E6r8pDTjWBHCwmEuRkdjynssf96k4"
CHAT_ID = "6259221563"

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
