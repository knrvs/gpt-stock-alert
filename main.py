import requests
import datetime

# 사용자 지정 값
BOT_TOKEN = "7805897776:AAG-c4E6r8pDTjWBHCwmEuRkdjynssf96k4"
CHAT_ID = "6259221563"

# 메시지 생성
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
message = f"📢 GPT 주식알리미 알림 테스트입니다.\n정상작동 확인 시간: {now}"

# 텔레그램 API URL
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
params = {
    "chat_id": CHAT_ID,
    "text": message
}

# 전송 요청
try:
    res = requests.post(url, params=params)
    res.raise_for_status()
    print("✅ 메시지 전송 성공")
except Exception as e:
    print(f"❌ 전송 실패: {e}")
